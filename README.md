# extended-map-test

A trial source for the MGU Store (iDrive 7): the CarPlay map laid under a layout on the whole instrument
cluster, tried without a laptop. Two components:

| id | kind | what |
|---|---|---|
| `akakingj_map_test` | app | **AK Map Test** (AK 지도 시험): one layout, KO 1 Map - KO 1's dials over the map laid under them. A copy of AK Cluster Layouts (akakingj/idrive7-cluster-info, branch personal-kr-extend, where it is developed and tested: `node tools/test_map_test.js`). Built on the head unit. |
| `waze-on-cluster` | tool | **Maps on cluster (extended map test)**, 0.10.901: Robert's Waze on cluster 0.10.9 with the map over or under a layout's window (`layout_window_file`, "under"), from akakingj/idrive-apps branch extend-map. Prebuilt and committed by the `build waze-on-cluster` workflow (native/waze-on-cluster.source.json). |

## 사용 순서 (차에서, 정차 상태)

1. Store 설정 > 소스 추가 > `akakingj/extended-map-test`.
2. Robert의 **Maps on cluster 앱**(`robertn_waze_cluster`)을 지우고, 이어서 **Maps on cluster 도구**(`waze-on-cluster` 0.10.x)를 지웁니다. (도구를 지우면 carplay·aapd 패치가 되돌려집니다.)
3. 이 소스의 **Maps on cluster (extended map test)** 도구를 설치합니다. (carplay 패치가 다시 걸리고 CarPlay가 재시작됩니다.)
4. Robert 소스에서 **Maps on cluster 앱**을 다시 설치합니다. (이미 깔린 0.10.901이 요구 조건을 채웁니다.)
5. 이 소스의 **AK Map Test**를 설치합니다. AK Cluster Layouts의 Show를 끄고, AK Map Test의 Show를 켭니다.

## 되돌리기

1. AK Map Test의 Show를 끄고(또는 앱을 지우고) AK Cluster Layouts의 Show를 켭니다.
2. Maps on cluster 앱 → 이 소스의 도구 순서로 지운 뒤, Robert 소스에서 도구와 앱을 다시 설치합니다.
3. 소스 `akakingj/extended-map-test`를 지웁니다.

While this tool is installed, Robert's updates of Waze on cluster do not arrive (the Store shows his listing
blocked: an installed component is updated only from the source that installed it).

## Licences

AK Map Test and kit/: as akakingj/idrive7-cluster-info (LICENSE, LICENSE-MIT, NOTICE.md).
native/waze-on-cluster: GPL-3.0-or-later (its LICENSE), Copyright (C) 2026 Robert Nisipeanu, the layout window
from eroobeeroo/idrive-apps 3b7ce93 (Copyright (C) 2026 eroobeeroo); source: akakingj/idrive-apps extend-map.
