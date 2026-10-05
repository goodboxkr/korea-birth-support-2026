# 2026 지역별 출산지원금 데이터 (시·도 / 시·군·구)

대한민국 17개 시·도와 시·군·구가 정부24(보조금24)에 등록한 **출산·임신 관련 지원 사업**을 지역별로 정리한 공개 데이터입니다.
모든 항목은 행정안전부 공공서비스 원문에서 그대로 옮겼고, 금액은 원문에 적힌 문구만 발췌했습니다(추정·가공 없음).

- 기준일: **2026년 10월 6일** 내려받은 원문
- 전체 1,082개 사업 · 시·도 17곳
- 원문 출처: 행정안전부 「대한민국 공공서비스(혜택) 정보」 — [공공데이터포털](https://www.data.go.kr/data/15113968/openapi.do) (공공누리 제1유형: 출처표시)
- 사람이 보기 쉬운 조회 화면: **[지역별 출산지원금 조회 — tools.newbizok.com](https://tools.newbizok.com/subsidy-birth/)**

## 시·도별 개수

| 시·도 | 출산 관련 지원 | 현금 지원 | 조회 페이지 |
|---|---:|---:|---|
| 서울 | 111 | 55 | [서울 출산지원금 조회](https://tools.newbizok.com/subsidy-seoul-birth/) |
| 부산 | 42 | 29 | [부산 출산지원금 조회](https://tools.newbizok.com/subsidy-busan-birth/) |
| 대구 | 28 | 12 | [대구 출산지원금 조회](https://tools.newbizok.com/subsidy-daegu-birth/) |
| 인천 | 38 | 26 | [인천 출산지원금 조회](https://tools.newbizok.com/subsidy-incheon-birth/) |
| 광주 | 33 | 16 | [광주 출산지원금 조회](https://tools.newbizok.com/subsidy-gwangju-birth/) |
| 대전 | 14 | 9 | [대전 출산지원금 조회](https://tools.newbizok.com/subsidy-daejeon-birth/) |
| 울산 | 28 | 15 | [울산 출산지원금 조회](https://tools.newbizok.com/subsidy-ulsan-birth/) |
| 세종 | 9 | 3 | [세종 출산지원금 조회](https://tools.newbizok.com/subsidy-sejong-birth/) |
| 경기도 | 178 | 92 | [경기도 출산지원금 조회](https://tools.newbizok.com/subsidy-gyeonggi-birth/) |
| 강원 | 53 | 33 | [강원 출산지원금 조회](https://tools.newbizok.com/subsidy-gangwon-birth/) |
| 충북 | 47 | 28 | [충북 출산지원금 조회](https://tools.newbizok.com/subsidy-chungbuk-birth/) |
| 충남 | 89 | 46 | [충남 출산지원금 조회](https://tools.newbizok.com/subsidy-chungnam-birth/) |
| 전북 | 87 | 48 | [전북 출산지원금 조회](https://tools.newbizok.com/subsidy-jeonbuk-birth/) |
| 전남 | 117 | 57 | [전남 출산지원금 조회](https://tools.newbizok.com/subsidy-jeonnam-birth/) |
| 경북 | 115 | 57 | [경북 출산지원금 조회](https://tools.newbizok.com/subsidy-gyeongbuk-birth/) |
| 경남 | 82 | 52 | [경남 출산지원금 조회](https://tools.newbizok.com/subsidy-gyeongnam-birth/) |
| 제주 | 11 | 6 | [제주 출산지원금 조회](https://tools.newbizok.com/subsidy-jeju-birth/) |

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
taken verbatim from the Ministry of the Interior and Safety public service data (KOGL Type 1). As of 2026-10-06. Lookup UI: https://tools.newbizok.com/subsidy-birth/

License: 원문 데이터는 공공누리 제1유형(출처표시), 정리 스크립트·구성은 CC BY 4.0.
