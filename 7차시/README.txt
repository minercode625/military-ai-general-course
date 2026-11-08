7차시 딥페이크와 AI 보안 — 만들어 보고, 구분해 보고, 뚫어 본다 (배포본)

7차시.pdf                          강의자료
prompts/00_README.txt              실습 파일 목록과 공통 규칙. 여기부터 읽는다.
prompts/01~11_*.txt                실습별 순서·기대 출력·기록표·안 될 때·집에서
notebook/deepfake_security.ipynb   오늘의 Colab 노트북(LLM 전용, 셀 3개: 준비 · 내 Gandalf · 숨은 명령). colab.research.google.com 에서
                                   "파일 > 노트 업로드"로 올린 뒤 "런타임 > 런타임 유형 변경 > T4 GPU" (필수).
notebook/make_images_optional.ipynb (선택) 글로 사진 만들기 — 집에서. 수업에서는 쓰지 않는다
docs/사례와_출처.txt               사례·통계·법령·가이드·실습 사이트 주소와 확인일
docs/규칙5줄_양식.txt              실습 7 양식
docs/가상얼굴/face_1~6.jpg         실습 2b 얼굴 바꾸기용 AI 가상 인물(실존 인물 아님). 이 6장만 올린다
docs/가상얼굴/video_1~2.mp4        실습 2c 영상 얼굴 바꾸기용 가상 인물 영상(4초). 이 2개만 올린다
docs/탐지용사진/                   실습 3 · 4용 사진 7장 — AI 5장(ai_1~4, ai_doc; sdxl-turbo) + 진짜 2장(real_1~2). 여기에 내가 바꾼 얼굴 1장을 더한다

FaceFusion 설치 파일(FaceFusion-Setup-3.9.1.exe + -1.bin, 약 1.7 GB)은 이 zip에 없다. 강사가 공유한 Google Drive 폴더
"7차시_FaceFusion_설치"에서 수업 전에 받아 같은 폴더에 둔다(prompts/01b_facefusion_install.txt).

얼굴 바꾸기는 docs/가상얼굴/ 의 AI 가상 인물로만 한다(본인·지인·유명인 금지). 사이트에 올리는 사진은 docs/탐지용사진/ 7장과 내가 바꾼 얼굴뿐이다.
공격 실습(프롬프트 인젝션)은 내 Colab의 내 AI와 공개 연습장에만 한다. 수업 끝에 바꾼 사진·영상은 지운다.
