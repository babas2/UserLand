MESAJ=TGᑌSEᖇᗷOT Avto Deploy"
MESAJ+="\nTELEGRAM: @UserBotTG"
pkg update -y
clear
echo -e $MESAJ
echo "Python yüklənir"
pkg install python -y
clear
echo -e $MESAJ
echo "Git yüklenir"
pkg install git -y
clear
echo -e $MESAJ
echo "TeleThon yüklenir"
pip install telethon
echo "Repo klonlanır"
git clone https://github.com/TheC0ala/TGUserBot
clear
echo -e $MESAJ
cd Qurulum
clear
echo "Kitabxana yüklənir"
echo -e $MESAJ
pip install wheel
pip install -r requirements.txt
python -m tg_installer.sh