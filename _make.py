# -*- coding: utf-8 -*-
"""공개 데이터 저장소 goodboxkr/korea-birth-support-2026 생성기 (외부유입 #5, 2026-10-06).
보조금24 원문(tools_24시약국/_data/gov24_services.json)을 _build_subsidy.py 와 같은 기준(theme_groups·amounts)으로 시·도별 출산 지원만 뽑는다.
다시 만들기: python _make.py  → git add -A; git commit; git push"""
import csv, datetime as dt, importlib.util, json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent / "tools_24시약국"
spec = importlib.util.spec_from_file_location("b", TOOLS / "_build_subsidy.py"); b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
DATA = TOOLS / "_data" / "gov24_services.json"
d = json.load(open(DATA, encoding="utf-8")); rows = d if isinstance(d, list) else d.get("data") or list(d.values())[0]
ds = dt.datetime.fromtimestamp(DATA.stat().st_mtime).date()
out, summ = [], []
for slug, name, _ in b.SIDO:
    loc, groups, order = b.theme_groups(rows, slug, "birth", name)
    cash = 0
    for gname in order:
        for r in groups[gname]:
            is_cash = (r.get("지원유형") or "").startswith("현금"); cash += is_cash
            out.append({"sido": name, "sigungu": "" if gname.endswith("전체") else gname, "service_name": r["서비스명"],
                        "agency": r.get("소관기관명") or "", "support_type": r.get("지원유형") or "",
                        "amounts_excerpt": " / ".join(b.amounts(r)), "deadline": b.clean(r.get("신청기한") or ""),
                        "target": b.clean(r.get("지원대상") or ""), "support": b.clean(r.get("지원내용") or ""),
                        "how_to_apply": (r.get("신청방법") or "").replace("||", " · "), "service_id": r.get("서비스ID") or "",
                        "gov24_url": r.get("상세조회URL") or f"https://www.gov.kr/portal/rcvfvrSvc/dtlEx/{r.get('서비스ID')}",
                        "lookup_page": f"{b.BASE}/subsidy-{slug}-birth/"})
    summ.append({"sido": name, "slug": slug, "count": len(loc), "cash_count": cash, "lookup_page": f"{b.BASE}/subsidy-{slug}-birth/"})
(HERE / "data").mkdir(exist_ok=True)
json.dump({"source": "행정안전부 「대한민국 공공서비스(혜택) 정보」(공공데이터포털, 공공누리 제1유형)", "downloaded": str(ds), "items": out},
          open(HERE / "data" / "birth_support_2026.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
with open(HERE / "data" / "birth_support_2026.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
with open(HERE / "data" / "summary_by_sido.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(summ[0])); w.writeheader(); w.writerows(summ)
tbl = "\n".join(f"| {s['sido']} | {s['count']} | {s['cash_count']} | [{s['sido']} 출산지원금 조회]({s['lookup_page']}) |" for s in summ)
(HERE / "README.md").write_text(f"""# 2026 지역별 출산지원금 데이터 (시·도 / 시·군·구)

대한민국 17개 시·도와 시·군·구가 정부24(보조금24)에 등록한 **출산·임신 관련 지원 사업**을 지역별로 정리한 공개 데이터입니다.
모든 항목은 행정안전부 공공서비스 원문에서 그대로 옮겼고, 금액은 원문에 적힌 문구만 발췌했습니다(추정·가공 없음).

- 기준일: **{ds.year}년 {ds.month}월 {ds.day}일** 내려받은 원문
- 전체 {len(out):,}개 사업 · 시·도 17곳
- 원문 출처: 행정안전부 「대한민국 공공서비스(혜택) 정보」 — [공공데이터포털](https://www.data.go.kr/data/15113968/openapi.do) (공공누리 제1유형: 출처표시)
- 사람이 보기 쉬운 조회 화면: **[지역별 출산지원금 조회 — tools.newbizok.com]({b.BASE}/subsidy-birth/)**

## 시·도별 개수

| 시·도 | 출산 관련 지원 | 현금 지원 | 조회 페이지 |
|---|---:|---:|---|
{tbl}

> 같은 사업이 보건소·구청마다 따로 등록된 경우가 있어, 실제로 한 사람이 받을 수 있는 개수와는 다를 수 있습니다. 광주·전남은 통합특별시 등록분을 양쪽에 함께 셉니다.

## 파일

| 파일 | 내용 |
|---|---|
| `data/birth_support_2026.csv` | 사업 1건 = 1줄 (UTF-8 BOM, 엑셀에서 바로 열림) |
| `data/birth_support_2026.json` | 같은 내용 JSON |
| `data/summary_by_sido.csv` | 시·도별 개수 요약 |

열 설명: `sido` 시·도, `sigungu` 시·군·구(빈칸 = 시·도 공통), `service_name` 사업명, `agency` 소관기관, `support_type` 지원유형,
`amounts_excerpt` 원문 금액 발췌, `deadline` 신청기한, `target` 지원대상, `support` 지원내용, `how_to_apply` 신청방법, `gov24_url` 정부24 원문, `lookup_page` 지역별 조회 페이지.

## 주의

- 지원 조건·금액·기한은 지자체 사정에 따라 바뀝니다. **신청 전에 반드시 `gov24_url`의 정부24 원문이나 주민센터에서 확인하세요.**
- 원문 신청기간이 지난해로 남아 있는 사업도 있습니다(지자체가 갱신하지 않은 경우).
- 오류 제보는 Issues로 남겨 주세요.

## English

Open dataset of childbirth/pregnancy support programs registered by Korean provincial and local governments on Gov24,
taken verbatim from the Ministry of the Interior and Safety public service data (KOGL Type 1). As of {ds}. Lookup UI: {b.BASE}/subsidy-birth/

License: 원문 데이터는 공공누리 제1유형(출처표시), 정리 스크립트·구성은 CC BY 4.0.
""", encoding="utf-8")
print(len(out), sum(s["count"] for s in summ)); [print(s["sido"], s["count"], s["cash_count"]) for s in summ]
