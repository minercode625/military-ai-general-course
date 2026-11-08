7차시 딥페이크와 AI 보안 — 실습 파일 목록과 공통 규칙
(군-학 연계 프로그램 범용 교육, 2026-10-28)

[파일]
01_colab_gpu_setup.txt      실습 0-1  Colab · T4 · 셀 1 미리 실행
01b_facefusion_install.txt  실습 0-2  FaceFusion 설치 (Google Drive 설치 파일, 관리자 권한 불필요)
02_detect_fakes.txt         실습 1    사람 눈으로 맞히기 (브라우저)
03_make_images.txt          (선택)    글로 사진 만들기 — 선택 노트북(집에서). 수업에서는 zip의 docs/탐지용사진/ 5장을 쓴다
03b_face_swap.txt           실습 2b   얼굴 바꾸기 — FaceFusion, AI 가상 인물 둘 + 기록표
03c_face_swap_video.txt     실습 2c   영상 얼굴 바꾸기 — FaceFusion + 보정 + 기록표
04_detector.txt             실습 3    AI 사진 탐지기에 넣어 보기 (브라우저) + 기록표
05_content_credentials.txt  실습 4    Content Credentials(C2PA) 확인 (브라우저)
06_my_gandalf.txt           실습 5    내 Gandalf — 비밀번호를 지키는 AI 뚫기 (셀 2) + 기록표
07_hidden_order.txt         실습 6    문서 속 숨은 명령 (셀 3)
08_five_rules.txt           실습 7    우리 조직 AI 사용 규칙 5줄
09_stuck.txt                안 될 때  증상별 조치 표
10_home.txt                 집에서    탐지기 20장 · LEVEL 5 · Prompt Airlines
11_prompt_airlines.txt      (선택)    공개 연습장 Prompt Airlines

[노트북]  notebook/deepfake_security.ipynb (메일로 받은 것과 같은 파일, LLM 전용 셀 3개) — Colab "파일 > 노트 업로드"로 올리고,
          "런타임 > 런타임 유형 변경 > T4 GPU"(필수). 셀 1 준비(실습 0-1) · 셀 2 내 Gandalf(실습 5) · 셀 3 숨은 명령(실습 6).
          notebook/make_images_optional.ipynb — (선택) 글로 사진 만들기, 집에서.
[문서]    docs/사례와_출처.txt (사례 · 법령 · 가이드 · 사이트 주소와 확인일), docs/규칙5줄_양식.txt
[사진 · 영상] docs/가상얼굴/face_1~6.jpg (실습 2b), video_1~2.mp4 (실습 2c) — AI(sdxl-turbo)가 만든 실존하지 않는 인물. 읽어주세요.txt
          docs/탐지용사진/ai_1~4.png · ai_doc.png (AI, sdxl-turbo · T4 · 2026-10-12) + real_1~2.jpg (진짜, Ultralytics 공개 샘플) — 실습 3 · 4에 올리는 7장. 읽어주세요.txt
[설치 파일] FaceFusion-Setup-3.9.1.exe + -1.bin — 이 zip에 없다. Google Drive 폴더 "7차시_FaceFusion_설치"에서 받는다(약 1.7 GB, 수업 전에).

[공통 규칙]
1. 셀은 위에서 아래로 하나씩 ▶. 바꾸는 줄은 "# <-- 바꿔 보세요" 줄뿐. 빨간 글씨는 두고 손을 든다. 5분 규칙.
2. 얼굴 바꾸기(실습 2b · 2c, FaceFusion)는 zip의 docs/가상얼굴/ AI 가상 인물 사진 6장 · 영상 2개로만. 본인 · 지인 · 연예인 · 정치인의 사진 · 영상은 넣지 않는다(내 PC 안에서만 돌아도 같다).
   (선택 노트북으로) 글로 사진을 만들 때도 사람 · 얼굴 · 실존 인물 · 로고를 넣지 않는다. 사물 · 풍경 · 문서만.
3. 사이트에 올리는 사진은 zip의 docs/탐지용사진/ 7장과 내가 FaceFusion으로 바꾼 사진뿐. 남의 사진 · 가족 사진 금지.
4. 공격(프롬프트 인젝션)은 내 Colab의 내 AI와 공개 연습장(Prompt Airlines)에만. 실제 서비스에 하면 범죄다.
5. 수업 끝에 풀어 둔 zip 사진과 바탕화면 FaceFusion_output 의 바꾼 사진 · 영상을 지운다. 남길 것은 기록표뿐.
6. 시간은 Colab T4 실측 기준(셀 1 약 1.6분). FaceFusion은 사진 2~15초, 4초 영상 2~5분(보정 포함, PC 성능에 따라). 브라우저 사이트는 무료 데모라 느리거나 잠들어 있을 수 있다(1분 기다린다).
