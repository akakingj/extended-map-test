# extended-map-test

A trial source for the MGU Store (iDrive 7): the CarPlay map laid under a layout on the whole instrument
cluster, tried without a laptop. Three components:

| id | kind | what |
|---|---|---|
| `akakingj_map_test` | app | **AK Map Test** (AK 지도 시험): one layout, KO 1 Map - KO 1's dials over the map laid under them. A copy of AK Cluster Layouts (akakingj/idrive7-cluster-info, branch personal-kr-extend, where it is developed and tested: `node tools/test_map_test.js`). Built on the head unit. |
| `waze-on-cluster` | tool | **Maps on cluster tool (extended map test)**, 0.10.901: Robert's Waze on cluster 0.10.9 with the map over or under a layout's window (`layout_window_file`, "under"), from akakingj/idrive-apps branch extend-map. Prebuilt and committed by the `build waze-on-cluster` workflow (native/waze-on-cluster.source.json). |
| `robertn_waze_cluster` | app | **Maps on cluster (extended map test)**, 0.6.12: Robert's Maps on cluster app as it is (robert/, a source package built on the head unit), so the tool and the app that controls it come from this one source. |

The renderer (`cluster-render`) and the Store's own tools stay Robert's: every cluster app needs them.

## 사용 순서 (차에서, 정차 상태)

1. Store 설정 > 소스 추가 > `akakingj/extended-map-test` (브랜치 main). Robert 소스는 그대로 둡니다.
2. Robert의 **Maps on cluster 앱**(0.6.x)을 지웁니다.
3. Robert의 **Maps on cluster 도구**(0.10.x)를 지웁니다. (carplay·aapd 패치가 되돌려집니다.)
4. 이 소스의 **Maps on cluster tool (extended map test)** 0.10.901을 설치합니다. (carplay 패치가 다시 걸리고 CarPlay가 재시작됩니다.)
5. 이 소스의 **Maps on cluster (extended map test)** 앱을 설치합니다.
6. 이 소스의 **AK Map Test**(AK 지도 시험)를 설치합니다. AK Cluster Layouts의 Show를 끄고, AK Map Test의 Show를 켭니다.

(2번을 건너뛰면 5번의 앱이 `robertn_waze_cluster2`로 옆에 하나 더 깔립니다: 먼저 지웁니다.)

## 되돌리기

1. AK Map Test의 Show를 끄고(또는 앱을 지우고) AK Cluster Layouts의 Show를 켭니다.
2. 이 소스의 Maps on cluster 앱 → 도구 순서로 지운 뒤, Robert 소스에서 도구와 앱을 다시 설치합니다.
3. 소스 `akakingj/extended-map-test`를 지웁니다.

While this tool is installed, Robert's updates of Waze on cluster and of its app do not arrive (the Store shows
his listings blocked: an installed component is updated only from the source that installed it).

## Licences

AK Map Test and kit/: as akakingj/idrive7-cluster-info (LICENSE, LICENSE-MIT, NOTICE.md).
native/waze-on-cluster and robert/robertn_waze_cluster: GPL-3.0-or-later (their LICENSE), Copyright (C) 2026 Robert Nisipeanu, the layout window
from eroobeeroo/idrive-apps 3b7ce93 (Copyright (C) 2026 eroobeeroo); source: akakingj/idrive-apps extend-map.
