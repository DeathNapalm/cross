# cross
script for parsing and uploading catalogs

Prerequisites:

google chrome ( yes, itś possible to install chrome on server os)
https://blog.softhints.com/ubuntu-16-04-server-install-headless-google-chrome/

wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb
sudo dpkg -i google-chrome-stable_current_i386.deb

webdriver:

http://chromedriver.chromium.org/getting-started

selenium:

pip install selenium



Configuration:
file credentials.txt is self-explanitory

как работает:
заходит на сайт в раздел загрузки
для каждого каталога перепарсивает его и скачивает
удаляет самые старые версии спарсенных каталогов( оставляет новые перепарсенные)

Скрипт отрабатывает линейно(пока) поэтому может выполняться долгое время

для запуска на сервере без gui раскомментить 34 строчку

Для запуска скрипта: 
python parsenew.py


Чек-лист проекта:

скачивать каталоги с сайта я cloudparser  done
перепарсивать скачанные каталоги с добавлением категорий и прочим   in progress
загружать переделанные каталоги в cms       in progress
