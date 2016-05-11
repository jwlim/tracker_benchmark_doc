# tracker_benchmark_doc

컴파일
------

명령어:
- make html 시 build directory에 html 파일들 생성

Build Directory:
- scripts/config.py의 'BUILD_DIR' 과
- Makefile의 'BUILDDIR' (windows의 경우 make.bat의 'BUILDDIR')
- 위의 두 변수 값을 동일하게 수정

소스파일
--------

index.html:
- source/index.rst

datasets.html:
- source/datasets.rst
- source/datasets/attributes/src_attribute.txt : dataset의 attribute 리스트와 description
- source/datasets/seq1/src_items.txt : tb50 sequences
- source/datasets/seq2/src_items.txt : 나머지 tb100 sequences

benchmark.html:
- source/benchmark.rst
- source/benchmark/src_overlap_*.txt : 벤치마크 스코어 테이블 생성을 위한 점수 리스트
- source/benchmark/trackers/src_trackers.txt : 벤치마크 트래커 리스트

 ```
  'Name'\t'Code'\t'Reference' 순으로 입력, reference 에 '[www]'\t'Link' 로 입력
  IVT IVT D.Ross, J. Lim, R.-S. Lin, and M.-H. Yang. Incremental Learning for Robust Visual Tracking. IJCV, 77(1):125–141, 2008. [www] http://www.cs.toronto.edu/~dross/ivt/
 ```

theme (sphinx_bootstrap_theme 사용):
- source/sphinx_bootstrap_theme/bootstrap/navbar.html : 홈페이지 상단 navigation bar
- source/_templates/layout.html : 전체 페이지에서 로드하는 페이지 (현재는 benchmark에서 테이블 소트용 javascript)
- source/_static/custom.css : 전체 페이지에 사용되는 css 파일
- source/_static/jquery.tablesorter.min.js : 테이블 소트용 javascript
- source/_static 내부의 파일들이 build 디렉토리의 _static 폴더로 복사 됨

scripts:
- rst 파일에서 사용되는 테이블을 자동으로 만들도록 하는 스크립트 (테이블 및 sub_*.rst 파일 등 생성)
