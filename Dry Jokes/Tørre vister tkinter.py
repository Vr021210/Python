import tkinter as tk
import customtkinter as ctk
from random import randint

root = ctk.CTk()

root.geometry("1920x1080")
root.title("Tørre Vitser 1.0")
ctk.set_appearance_mode("system")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("blue")

vits1 = "Hei, pass deg for den den landminen! – Pøh, og den tror du jeg går på…."
vits2 = "Har du hørt om han som reklamerte på den nye kortstokken han hadde kjøpt? – Fire av kortene var knekt…"
vits3 = "Vet du hva som står på på utgangsdøren i sædbanken? – Takk for at du kom…"
vits4 = "Har du hørt om han som ikke klarte å komme på hva støv betød på engelsk? – Han følte seg ganske dust.."
vits5 = "Har du hørt om han som ikke likte kaffe? – Han syntes ikke det var noe å trakte etter…"
vits6 = "Vet du hva moren til Pinocchio var? – Trebarnsmor…"
vits7 = "Man kan si mye rart om Sveits, men en ting er i hvert fall sikkert. – Flagget er et stort pluss…"
vits8 = "Har du hørt om appelsinen som ble til appelsinjuice? – Den følte seg presset til det…"
vits9 = "Har du hørt om eselet som skrek så høyt at det ble hest?"
vits10 = "En far vasker bilen med sønnen. Så spør sønnen «Hvorfor kan du ikke bare bruke en svamp?»"
vits11 = "Hvorfor bør du ikke pusse tennene med venstrehånda? Det er bedre å bruke en tannbørste."
vits12 = "Hvorfor fikk ikke eplet komme inn på utestedet? – Fordi dørvakta var eplenektar"
vits13 = "Eple nekta, de kneip brødet, men sikta hvetemelet"
vits14 = "Jeg pleier å be ungene om å stille seg i hjørnet om de klager på at det er kaldt, er jo 90 grader der."
vits15 = "Hva kaller du to soldater som holder hender? – Leiesoldater"
vits16 = "Hvorfor døde mammutene ut? Det var ingen papputer igjen."
vits17 = "«Kan du kjøpe en kiste?» – «Nei! Det er det siste jeg skal kjøpe.»"
vits18 = "Hvilket land har kommet lengst innen romfart? – Norge, siden vi er det eneste landet i verden med flyplass på Sola."
vits19 = "Kona fant en edderkopp i boden, og spurte om jeg kunne ta den med ut. Så vi tok et par øl på puben, hyggelig fyr… Han er web designer…"
vits20 = "Ingenting slår å legge fram gaffel ved sia av suppeskåla til dattera, når hun oppdager feilen sier jeg «Ja, sånt kan skje den beste.» Like artig hver mandag."
vits21 = "Hvorfor har elgen horn? Fordi det ville sett dumt ut med rundstykker."
vits22 = "Hvorfor blir eplene til juice? De blir presset til det.."
vits23 = "Vet du hvem som har ansvaret for melkesalget i Saudi-Arabia? – Milksjeiken"
vits24 = "Hvorfor har ikke isbiter armer og bein? – De er vannskapte"
vits25 = "Er en kar nedi gata vår som sliter veldig med hjernerystelser. Han bor et steinkast unna."
vits26 = "Hvorfor kan man ikke forsove seg som skuespiller? Du må alltid opptre."
vits27 = "Og så var det skredderen som var stoffmisbruker."
vits28 = "Hva kaller du en fisk som tenker sjæl? – Filosofisk"
vits29 = "Hørt om elgen som gikk i vannet og ble rein, så ble han skutt og da sa jegeren «hjort er hjort»"
vits30 = "En mann kjøpte en klokke. Så ventet han til den ble to, og så solgte han den andre."
vits31 = "Sønn: Pappa, kan du ta på skoene mine? Pappa: Det kan jeg, men jeg tror ikke de vil passe."
vits32 = "Kan være at jeg er innbillsk altså, men jeg er rimelig sikker på at resepsjonisten på hotellet sjekket meg ut."
vits33 = "Hva spiser spøkelser til frokost? – Bøskiver."
vits34 = "Det var en gang. Og innafor var det et kjøkken."
vits35 = "Har du hørt om fuglen som spiste snø? – Den hadde hørt at den kunne få mark i magen."
vits36 = "Da jeg var liten ble jeg vaksinert mot kopper. Derfor drikker jeg nå alltid rett fra flasken."
vits37 = "Hva heter opplysningskontoret for kuer? – Q-tips."
vits38 = "Hvorfor liker ikke Knerten å sove på magen? – Han liker ikke å våkne opp på mårrakvisten."
vits39 = "Hva sa den ene snømannen til den andre? “Er det bare meg eller lukter det litt gulrot her?"
vits40 = "Den ene tørrfisken sa til den andre: – Long time no sea."
vits41 = "Hva slags musikk hører osten på? – Ostepop."
vits42 = "Hvilken hunderase drikker mest vann? – Olden Retriever."
vits43 = "Hva spiser datamaskinen på julaften? – Minnepinnekjøtt"
vits44 = "Hørt om reka på loffen?"
vits45 = "Jammen er seilbåter i vinden om dagen!"
vits46 = "Hva sa svensken da han fikk en murstein i hodet? – Jättekul"
vits47 = "Hørt om tyven som stjal en kalender? – Han fikk 12 måneder."
vits48 = "Jeg trener nesten hver dag. Som i dag for eksempel, da trente jeg nesten."
vits49 = "For to år siden sa legen min at jeg var på tur til å bli døv. – Jeg har ikke hørt fra ham siden."
vits50 = "Hørt om svensken som drev et datingbyrå for ender? Dessverre var det vanskelig å få endene til å møtes."
vits51 = "Vet du hva Blodbanken Oslo sin siste kampanje er? – Verv en ven"
vits52 = "Hva heter foreldrene til Tarzan? – Morzan og Farzan"
vits53 = "Hva har en svidd pizza og en gravid kvinne til felles? – En mann har glemt å ta den ut i tide."
vits54 = "I dag leste jeg en bok om lim. – Jeg klarte ikke å legge den fra meg."
vits55 = "Hvorfor har brannmenn røde bukseseler? – For å holde buksene oppe."

vitser = [
    vits1, vits2, vits3, vits4, vits5, vits6, vits7, vits8, vits9, vits10,
    vits11, vits12, vits13, vits14, vits15, vits16, vits17, vits18, vits19, vits20,
    vits21, vits22, vits23, vits24, vits25, vits26, vits27, vits28, vits29, vits30,
    vits31, vits32, vits33, vits34, vits35, vits36, vits37, vits38, vits39, vits40,
    vits41, vits42, vits43, vits44, vits45, vits46, vits47, vits48, vits49, vits50,
    vits51, vits52, vits53, vits54, vits55
]

def generate():
    vits = vitser[randint(0, len(vitser) - 1)]
    vitslabel.configure(text=vits)

welcomelabel = ctk.CTkLabel(master=root, text="Tørre Vitser!😂", font=('Arial', 18))
button = ctk.CTkButton(master=root, text="Gi meg en vits!", font=('Arial', 18), corner_radius=16, command=generate)
vitslabel = ctk.CTkLabel(master=root, text="", font=('Arial', 18))

welcomelabel.pack(pady=10)
button.pack(pady=50)
vitslabel.pack(pady=10)

root.mainloop()
