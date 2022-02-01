python3 machinetag.py -a >a.txt
asciidoctor a.txt
asciidoctor-pdf -a allow-uri-read  a.txt
cp a.html ../../misp-website/static/taxonomies.html
cp a.pdf ../../misp-website/static/taxonomies.pdf
scp a.html circl@cpab.circl.lu:/var/www/nwww.circl.lu/doc/misp-taxonomies/index.html
scp a.pdf circl@cpab.circl.lu://var/www/nwww.circl.lu/doc/misp-taxonomies/taxonomies.pdf
