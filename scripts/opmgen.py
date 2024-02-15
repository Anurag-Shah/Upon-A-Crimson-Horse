import random

common = '''#%s

graphical_culture = muslimgfx

color = { %s %s %s }

historical_idea_groups = {
	defensive_ideas
	religious_ideas
	offensive_ideas
	trade_ideas
	spy_ideas
	economic_ideas
	diplomatic_ideas
	administrative_ideas
}

historical_units = {
	persian_footsoldier
	persian_cavalry_charge
	persian_shamshir
	qizilbash_cavalry_unit
	tofongchis_musketeer
	topchis_artillery
	afsharid_reformed
	afsharid_reformed_infantry
	muslim_mass_infantry
	muslim_dragoon
	persian_rifle
}

monarch_names = {
	"Joneid #0" = 10
	"Haidar #0" = 10
	"Ismâ'îl #0" = 10
	"Tamâshp #0" = 10
	"Mohammad Kodabânda #0" = 10
	"'Abbâs #0" = 10
	"Safi #0" = 10
	"Solaymân #0" = 10
	"Hosayn #0" = 30
	"Kulu #0" = 30
	"Sulaymanshah #0" = 30
	"Farid #0" = 30
	"Sayf #0" = 30
	"Ebrâhim #0" = 10
	"Jalal #0" = 20
	"Tarum #0" = 20
	"Gurgin #0" = 20
	"Shâh Rukh #0" = 10
	"Nâder Mirza #0" = 10
	"Karim #0 Khân" = 10
	"Abu'l Fath #0" = 10
	"Mohammad Ali #0" = 10
	"Mohammad Sâdiq #0" = 10
	"'Ali Morâd #0" = 10
	"Ja'far #0" = 10
	"Loft Ali #0" = 10
	"Aga Muhammad #0" = 10
	"Fath Alî #0" = 10
	"Najm-e #0" = 0
	"Ahmad #0" = 0
	"Hatem #0" = 0
	"Shahqoli #0" = 0
	"Rajab Ali #0" = 0
	"Farajollah #0" = 0
	"Amanollah #0" = 0
	"Ebrahim #0" = 0
	"Ali #0" = 0
	"Allahyar #0" = 0
	"Abdol #0" = 0
	"Hamid #0" = 0
	
	"Atiya #0" = -1
	"Pari #0" = -1
	"Khayr al-Nisa #0" = -1
	"Tajlu #0" = -1
	"Dilaram #0" = -1
	"Shahbanu #0" = -1
	"Razia #0" = -1
	"Maryam #0" = -1
}

leader_names = {
	Sharbatdar
	Qassab
	Kamal
	Farrukhshah
	Kudkkhani
	Tarumi
	Lari
	Sariq
	Sabiri
	Jalili
	Azizi
	Shahy
	Qazai
	Ahrari
	Fatemi
	Sabet
	Ansari
}

ship_names = {
	Abathur "Adamn Kasia" "Aesma Daeva" Agas
	Ahriman Ahura "Ahura Mazda" Ahurani Airyaman
	"Aka Manah" Aladdin Allatum Amashaspan Ameratat
	"Amesha Spentas" Anahita "Angra Mainyu" Anjuman
	"Apam-natat" Apaosa Aredvi Arishtat Armaiti Arsaces
	"Asha vahista" Asman "Asto Vidatu" "Astvat-Ereta"
	Atar "Azi Dahaka" Baga Bahram Burijas Bushyasta Buyasta
	Camros Daena Daevas Ahaka Dahhak Dena Dev Diwe Drug
	Drvaspa Frashegird Fravashis Gandarewa "Gao-kerena"
	Gayomard Gayomart "Geus-Tasan" "Geus-Urvan" Haoma
	Haurvatat Humay Hvar Hvarekhshaeta Indar Indra Izha
	Jamshid Jeh Karshipta Kavi Khara "Khshathra vairya"
	Kundrav Mah Mahre Mahrianag Manu Manuchihir Mao 
	Mashyane Mashye Menog Mithra Nairyosangha Nanghaithya
	Neriosang Ormazd Peris Peshdadians Rapithwin Rashnu
	Rustam Saurva Simurgh "Spenta Mainyu" Sraosa Srosh
	Tawrich Thunaupa Tistrya Tushnamatay Vanant Vata
	Verethragna "Vohu Manah" Vouruskasha Yam Yasht Yazata
	Yezidi Yima Zal Zam "Zam-Armatay" Zarathustra Zarich
	"Zend-Avesta" Zurvan
}
'''

history = '''#%s
government = monarchy
add_government_reform = uach_governor
government_rank = 1
primary_culture = persian
religion = shiite
technology_group = muslim
capital = %s
'''

lis = [["415", "Kirkuk"], ["4294", "Sulaimaniyah"], ["2211", "Sanandaj"], ["2209", "Ilam"], ["2210", "Kirmanshah"], ["413", "Khorrambad"], ["4289", "Shushtar"], ["414", "Hamadan"], ["4300", "Mianeh"], ["2212", "Zanjan"], ["4338", "Soltanieh"], ["2215", "Qazvin"], ["428", "Teheran"], ["4337", "Savah"], ["2213", "Qom"], ["2216", "Semnan"], ["4335", "Kashan"], ["4171", "Abarquh"], ["2222", "Ardakan"], ["4342", "Malamir"], ["2217", "Yasuj"], ["430", "Dashtistan"], ["4331", "Kazerun"], ["2218", "Shiraz"], ["4329", "Fasa"], ["4330", "Darab"], ["2234", "Rafsanjan"], ["4345", "Saidabad"], ["2220", "Bam"], ["435", "Zaranj"], ["2230", "Chakhansur"], ["2229", "Bust"], ["447", "Kandahar"], ["448", "Gazni"], ["451", "Kabul"], ["2226", "Jalalabad"], ["578", "Peshawad"], ["427", "Damghan"], ["2235", "Sabzevar"], ["2214", "Esterabad"], ["4334", "Tabas"], ["4336", "Tun"], ["436", "Birjand"], ["4326", "Nishapur"], ["2221", "Mashhad"], ["4325", "Sarakhs"], ["2350", "Konjikala"], ["445", "Marw al-Shahijan"], ["4324", "Ghuriyan"], ["2224", "Ferah"], ["449", "Baghlan"], ["2225", "Bamyan"], ["2228", "Maymana"], ["4343", "Termez"], ["4344", "Kish-Shakhrisabz"], ["1968", "Kulob"], ["444", "Charjuy"], ["453", "Qarshi"], ["454", "Samarkand"], ["458", "Kokand"], ["1967", "Khujand"], ["457", "Tashkent"], ["2356", "Shymkent"], ["2363", "Atakent"], ["455", "Kermine"], ["2362", "Gurganj"], ["2370", "Kungirot"], ["440", "Shimbay"], ["1973", "Urgench"]]

loc = ""

for i, item in enumerate(lis):
    tag = f"U{str(i).rjust(2, '0')}"
    name = item[1]
    id = item[0]

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    thist = history % (f"UACH opm governor: {tag} - {name}", id)
    tcomm = common % (f"UACH opm governor: {tag} - {name}", r, g, b)
    tct = f'{tag} = "countries/{name}.txt"'

    with open(f"history/{tag} - {name}.txt", "w") as hf:
        hf.write(thist)
    with open(f"common/{name}.txt", "w") as hf:
        hf.write(tcomm)
    print(tct)
    loc += f' {tag}: "{name}"\n'
    loc += f' {tag}_ADJ: "{name}an"\n'
    loc += f' {tag}_ADJ2: "{name}an"\n'

with open("loc.txt", "w") as lo:
    lo.write(loc)