
# Fecha en formato 20131218
fecha=$(date +"%Y%m%d")
#echo sarasa_${fecha}

cd portfolioPersonal

rm output/output_${fecha}
scrapy crawl portfolioPersonal -a ppUser=pepe -a ppPassword=fruta -o output/output_${fecha}

cd ..
python processData.py output_${fecha}
