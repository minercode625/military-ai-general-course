6차시 sLLM 파인튜닝 — 작은 공개 LLM을 내 데이터로 학습시키기 (배포본)

6차시.pdf                     강의자료
prompts/00_README.txt         실습 파일 목록과 공통 규칙. 여기부터 읽는다.
prompts/01~12_*.txt           실습별 순서·기대 출력·기록표·안 될 때
notebook/sllm_finetune.ipynb  오늘의 Colab 노트북. colab.research.google.com 에서 열고
                              "파일 > 노트 업로드"로 올린 뒤 "런타임 > 런타임 유형 변경 > T4 GPU" (필수).
docs/data/service_200.jsonl   고객센터 응대 200쌍 (학습 데이터, 노트북 셀 3 안에 같은 내용이 들어 있음)
docs/data/rules_100.jsonl     사내 규정집 Q&A 100쌍
docs/data/미리보기.txt         데이터 모양 미리보기
docs/mint_rules.txt           민트상사 사내 규정집(3차시 문서). 실습 1·5·7의 정답 대조용

모든 데이터는 가상 회사(민트상사)의 가상 데이터다. 실제 업무 자료·개인정보는 올리지 않는다.
학습한 어댑터 mint_lora.zip 은 수업 끝에 노트북 셀 9로 내려받는다(세션이 끝나면 사라진다).
