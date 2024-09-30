#!/usr/bin/env perl

# 参考: http://www2.yukawa.kyoto-u.ac.jp/~koudai.sugimoto/dokuwiki/doku.php?id=latex:latexmk%E3%81%AE%E8%A8%AD%E5%AE%9A

# %Sはソースファイル、%Oはオプション、%Dは出力ファイルに置き換えられます（もし指定しなくてもlatexmkが自動的に補完してくれる）

# LaTeX
# -synctex=1: プレビュー画面からソースコードの該当箇所に移動できる
# -halt-on-error: コンパイル中にエラーが発生した場合、コンパイルを終了する
# -file-line-error: 何行目でエラーが出たかを表示
$latex = 'platex -synctex=1 -halt-on-error -file-line-error %O %S';
$max_repeat = 5;

# BibTeX
$bibtex = 'pbibtex %O %S';
$biber = 'biber --bblencoding=utf8 -u -U --output_safechars %O %S';

# index
$makeindex = 'mendex %O -o %D %S';

# DVI / PDF
# -o %D: dvi と同じ階層に pdfファイルを作成する
$dvipdf = 'dvipdfmx %O -o %D %S';
$pdf_mode = 3;

# preview
$pvc_view_file_via_temporary = 0;
if ($^O eq 'linux') {
    $dvi_previewer = "xdg-open %S";
    $pdf_previewer = "xdg-open %S";
} elsif ($^O eq 'darwin') {
    $dvi_previewer = "open %S";
    $pdf_previewer = "open %S";
} else {
    $dvi_previewer = "start %S";
    $pdf_previewer = "start %S";
}

# clean up
$clean_full_ext = "%R.synctex.gz"
