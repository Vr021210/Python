import tkinter as tk
import customtkinter as ctk

root = ctk.CTk()
root.title("InformasjonsTeknologi og MedieProduksjon")
root.geometry("1920x1080")

skoler = """
Skoler + Snittkrav:
Bjørnholt: 2,04
Elvebakken StudieKompetanse: 4,76
Elvebakken Uten StudieKompetanse: 4,50
Fyrstikkalleen: 3,92
Kuben: 3,63
"""
skolerframe = ctk.CTkFrame(root,corner_radius=10)


def clearallitems():
    for widget in root.winfo_children():  # Loop through all widgets in the frame
        widget.pack_forget()  # Remove them from the layout

def showmainpage():
    clearallitems()
    mainpage_title.pack()
    skoler_button.pack(pady=10)
    muligejobbermainpagebutton.pack()
    videretdanningbutton.pack(pady=10)
    
    
    backtomainpagebutton.pack(side="bottom",anchor="sw",pady=10)
    genereltOmIMframe.pack(side="top", fill="both", padx=10, pady=10,expand=True)
    genereltOmIMlabel.pack(side="top", anchor="w", padx=5, pady=5)
    genereltOmIM.pack(side="top", anchor="w", padx=5, pady=5)

def showskolerpaige():
    clearallitems()
    backtomainpagebutton.pack(side="bottom",anchor="sw",pady=10)
    skolerframe.pack(side="top", fill="both", padx=10, pady=10,expand=True)
    skoler_label.pack(side="top", anchor="w", padx=5, pady=5)

def showmuligejobberpage():
    clearallitems()
    backtomainpagebutton.pack(side="bottom",anchor="sw",pady=10)
    velgretningframe.pack()
    velgenavstudieretningenelabel.pack()
    ITretning1button.pack()
    MPretning1button.pack()

def it_jobber_page():
    clearallitems()
    backtomainpagebutton.pack(side="bottom",anchor="sw",pady=10)
    itjobber_frame.pack()
    itdriftsteknikerbutton.pack()
    itutviklerbutton.pack()

def medieproduksjonpage():
    clearallitems()
    backtomainpagebutton.pack(side="bottom",anchor="sw",pady=10)
    medieproduksjonsjobberframe.pack(pady=10)
    innholdsprodusentbutton.pack()
    mediedesignerbutton.pack()
    medieteknikerbutton.pack(pady=10)

def itdriftsteknikerpage():
    clearallitems()
    backtomainpagebutton.pack(side="bottom",anchor="sw",pady=10)
    itdriftteknikernødvendigutdanningframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    itdriftteknikernødvendigutdanninglabel.pack()
    inforamsjonsteknologiførsteår.pack(pady=10)
    informasjonsteknologiandreår.pack(pady=10)
    informasjonsteknologitredjeår.pack(pady=10)
    itdriftsteknikermuligeoppghaverframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    itdriftsteknikermuligeoppghaverlabel.pack()
    itdriftsteknikermuligeoppghaver.pack()
    itdriftteknikerpersonligeegenskaperframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    itdriftteknikerpersonligeegenskaperlabel.pack()
    itdriftteknikerpersonligeegenskaper.pack()
    itdriftteknikeraktueltarbeidsstedframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    itdriftteknikeraktueltarbeidsstedlabel.pack()
    itdriftteknikeraktueltarbeidssted.pack()

def itutviklerpage():
    clearallitems()
    backtomainpagebutton.pack(side="bottom",anchor="sw",pady=10)
    itutviklerutdanningframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    itutviklerutdanning.pack()
    itutviklerutdanningførsteår.pack(pady=10)
    itutviklerutdanningandreår.pack(pady=10)
    itutviklerutdanningtredjeogfjerdeår.pack(pady=10)
    itutviklermuligeoppgaverframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    ututviklermuligeoppgaverbiglabel.pack()
    itutviklermuligeoppgaverlabel.pack()
    itutviklerpersonligeegenskaperframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    itutviklerpersonligeegenskaperlabel.pack()
    itutviklerpersonligeegenskaper.pack()
    itutvikleraktueltarbeidsstedframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    itutvikleraktueltarbeidsstedlabel.pack()
    itutvikleraktueltarbeidssted.pack()

def innholdsprodusentpage():
    clearallitems()
    backtomainpagebutton.pack(side="bottom",anchor="sw",pady=10)
    innholdsprodusentframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    innholdsprodusentnødvendigutdanning.pack()
    innholdsprodusentførsteår.pack(pady=10)
    innholdsprodusentandreår.pack(pady=10)
    innholdsprodusenttredjeår.pack(pady=10)
    innholdsprodusentmuligeoppgaverframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    innholdsprodusentmuligeoppgaverlabel.pack()
    innholdsprodusentmuligeoppgaver.pack()
    innholdsprodusentPEframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    innholdsprodusentPElabel.pack()
    innholdsprodusentPE.pack()
    innholdsprodusentaktueltarbeidsstedframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    innholdsprodusentaktueltarbeidsstedlabel.pack()
    innholdsprodusentaktueltarbeidssted.pack()

def mediedesignerpage():
    clearallitems()
    backtomainpagebutton.pack(side="bottom",anchor="sw",pady=10)
    mediedesignernødvendigutdanningframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    mediedesignernødvendigutdanninglabel.pack()
    mediedesignernødvendigutdanningførsteår.pack(pady=10)
    mediedesignernødvendigutdanningandreår.pack(pady=10)
    mediedesingernødvendigutdanningtredjeår.pack(pady=10)
    mediedesignermuligeoppgaverframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    mediedesignermuligeoppgaverlabel.pack()
    mediedesignermuligeoppgaver.pack()
    mediedesignerpersonligeegenskaperframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    mediedesignerperonligeegenskaperlabel.pack()
    mediedesignerpersonligeegenskaper.pack()
    mediedesigneraktueltarbeidsstedframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    mediedesigneraktueltarbeidsstedlabel.pack()
    mediedesigneraktueltarbeidssted.pack()

def medieteknikerpage():
    clearallitems()
    backtomainpagebutton.pack(side="bottom",anchor="sw",pady=10)
    medieteknikernødvendigutdanninglabel.pack()
    medieteknikernødvendigutdanningframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    medieteknikernødvendigutdanningførsteår.pack(pady=10)
    medieteknikernødvendigutdanningandreår.pack(pady=10)
    medieteknikernødvendigutdanningtredjeår.pack(pady=10)
    medieteknikermuligeoppgaverframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    medieteknikermuligeoppgaverlabel.pack()
    medieteknikermuligeoppgaver.pack()
    medieteknikerpersonligeegenskaperframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    medieteknikerpersonligeegenskaperlabel.pack()
    medieteknikerpersonligeegenskaper.pack()
    medieteknikeraktueltarbeidsstedframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    medieteknikeraktueltarbeidsstedlabel.pack()
    medieteknikeraktueltarbeidssted.pack()

def videreutdanningpage():
    clearallitems()
    backtomainpagebutton.pack(side="bottom",anchor="sw",pady=10)
    videreutdanningframe.pack(side="top", fill="both", padx=10, pady=5,expand=True)
    videreutdanninglabel.pack()
    videreutdanning.pack()

def fagfordelingpage():
    clearallitems()
    backtomainpagebutton.pack(side="bottom",anchor="sw",pady=10)

videretdanningbutton = ctk.CTkButton(root, text="Videreutdanning", command=videreutdanningpage,hover_color="green")
videreutdanningTEXT = """
Yrkesfaglig opplæring fører fram til yrkeskompetanse (med eller uten fag- eller svennebrev). Etter fullført yrkesfaglig opplæring kan du gå ut i arbeid eller ta videre utdanning:

Du kan ta videre utdanning på fagskole. En fagskoleutdanning er en kort og yrkesrettet høyere utdanning som er beregnet på de som har gått yrkesfag.
Du kan ta Vg3 påbygging til generell studiekompetanse
etter Vg2 eller
etter oppnådd yrkeskompetanse.
Da har du mulighet til å ta høyere utdanning ved høyskole eller universitet. Husk at noen studier, f.eks. ingeniør-, realfags- og medisinske studier, forutsetter at du har visse realfag.
Du kan også søke opptak til høyere utdanning etter forkurs eller gjennom «Y-veien» (yrkesfaglig vei). Y-veien er beregnet på deg som har relevant yrkeskompetanse. Forkurs og Y-veien er vanligst innen realfags- og ingeniørstudier.
"""
videreutdanningframe = ctk.CTkFrame(root,corner_radius=10)
videreutdanninglabel = ctk.CTkLabel(videreutdanningframe, text="Videreutdanning", font=("Arial", 40))
videreutdanning = ctk.CTkLabel(videreutdanningframe,text=videreutdanningTEXT, font=("Arial", 14))





genereltOmIMTEXT = """
Du lærer:
idéutvikling og kreativ problemløsning
om brukerstøtte, nettverk, IT-sikkerhet og programmering
innholdsformidling og historiefortelling
foto, film og grafisk design
kommunikasjon og markedsføring


Du bør være:
kreativ
Interessert i IT, nettverk og programvare
interessert i visuelle uttrykksformer
nøyaktig


Du kan bli:
IT-utvikler eller IT-driftstekniker
mediedesigner, medietekniker eller medieprodusent


Arbeidssteder:
IT-driftsselskaper og IT-avdelinger
multimediebedrifter, reklamebyråer eller forlag
"""
genereltOmIMframe = ctk.CTkFrame(root,corner_radius=10)
genereltOmIMlabel = ctk.CTkLabel(genereltOmIMframe, text="Generelt Om InformasjonsTeknologi og MedieProduksjon", font=("Arial", 20))
genereltOmIM = ctk.CTkLabel(genereltOmIMframe, text=genereltOmIMTEXT, justify="left",font=("Arial", 15))

backtomainpagebutton = ctk.CTkButton(root, text="Tilbake", command=showmainpage, fg_color="red",hover_color="green")
mainpage_title = ctk.CTkLabel(root, text="InformasjonsTeknologi og MedieProduksjon", font=("Arial", 20))

skoler_button = ctk.CTkButton(root, text="Skoler", command=showskolerpaige,hover_color="green")

skoler_label = ctk.CTkLabel(skolerframe, text=skoler,font=("Arial", 30), justify="left")
muligejobbermainpagebutton = ctk.CTkButton(root, text="Mulige Jobber", command=showmuligejobberpage,hover_color="green")

mediedesignerbutton = ctk.CTkButton(root, text="Mediedesigner", command=mediedesignerpage,hover_color="green")
medieteknikerbutton = ctk.CTkButton(root, text="Medietekniker", command=medieteknikerpage,hover_color="green")

velgretningframe = ctk.CTkFrame(root,corner_radius=10)
velgenavstudieretningenelabel = ctk.CTkLabel(velgretningframe, text="Velg en av studieretningene", font=("Arial", 20))
ITretning1button = ctk.CTkButton(velgretningframe, text="Informasjonteknologi", command=it_jobber_page,hover_color="green")
MPretning1button = ctk.CTkButton(velgretningframe, text="Medieproduksjon", command=medieproduksjonpage,hover_color="green")

itjobber_frame = ctk.CTkFrame(root,corner_radius=10)

itdriftsteknikerbutton = ctk.CTkButton(itjobber_frame, text="IT-driftstekniker",command=itdriftsteknikerpage,hover_color="green")
itdriftteknikernødvendigutdanningframe = ctk.CTkFrame(root,corner_radius=10)
itdriftteknikernødvendigutdanninglabel = ctk.CTkLabel(itdriftteknikernødvendigutdanningframe, text="Nødvendig Utdanning", font=("Arial", 20))
inforamsjonsteknologiførsteår = ctk.CTkLabel(itdriftteknikernødvendigutdanningframe, text="Første år: Informasjonsteknologi Og medieproduksjon",fg_color="orange",corner_radius=10)
informasjonsteknologiandreår = ctk.CTkLabel(itdriftteknikernødvendigutdanningframe, text="Andre År: Informasjonsteknologi",fg_color="orange",corner_radius=10)
informasjonsteknologitredjeår = ctk.CTkLabel(itdriftteknikernødvendigutdanningframe, text="Tredje og fjerde år: IT-driftsfaget",fg_color="green",corner_radius=10)

itdtmo = """
planlegge og vurdere virksomhetens bruk av ny teknologi og IT-løsninger
drifte virksomhetens IT-systemer
installasjon, bruk og vedlikehold av programvare
opplæring og veiledning i bruk av IT-systemer
anvende og utvikle rutiner for virksomhetens IT-systemer
service og brukerstøtte
etikk og lovverk
"""

itdriftsteknikermuligeoppghaverframe = ctk.CTkFrame(root,corner_radius=10)
itdriftsteknikermuligeoppghaverlabel = ctk.CTkLabel(itdriftsteknikermuligeoppghaverframe, text="Mulige Oppgaver", font=("Arial", 20))
itdriftsteknikermuligeoppghaver = ctk.CTkLabel(itdriftsteknikermuligeoppghaverframe, text=itdtmo, justify="left",font=("Arial", 15))

itdtpersonligeegenskaper = """
Du må kunne arbeide systematisk og nøyaktig, både selvstendig og i
samarbeid med andre. Gode kommunikasjonsevner og god skriftlig og muntlig
framstilling på norsk og engelsk er viktig. Du bør ha evne til å tenke nytt, være
kreativ og interessert i ny teknologi.
"""
itdriftteknikerpersonligeegenskaperframe = ctk.CTkFrame(root,corner_radius=10)
itdriftteknikerpersonligeegenskaperlabel = ctk.CTkLabel(itdriftteknikerpersonligeegenskaperframe, text="Personlige Egenskaper", font=("Arial", 20))
itdriftteknikerpersonligeegenskaper = ctk.CTkLabel(itdriftteknikerpersonligeegenskaperframe, text=itdtpersonligeegenskaper, justify="left",font=("Arial", 15))

itdtaktueltarbeidssted = """
En it-driftstekniker jobber med drift av IT-systemer i alle typer virksomheter, offentlige og private.
"""

itdriftteknikeraktueltarbeidsstedframe = ctk.CTkFrame(root,corner_radius=10)
itdriftteknikeraktueltarbeidsstedlabel = ctk.CTkLabel(itdriftteknikeraktueltarbeidsstedframe, text="Aktuelt Arbeidssted", font=("Arial", 20))
itdriftteknikeraktueltarbeidssted = ctk.CTkLabel(itdriftteknikeraktueltarbeidsstedframe, text=itdtaktueltarbeidssted, justify="left",font=("Arial", 15))

itutviklerbutton = ctk.CTkButton(itjobber_frame, text="IT-utvikler",command=itutviklerpage,hover_color="green")



itutviklerutdanningframe = ctk.CTkFrame(root,corner_radius=10)

itutviklerutdanning = ctk.CTkLabel(itutviklerutdanningframe, text="Nødvendig Utdanning", font=("Arial", 20))
itutviklerutdanningførsteår = ctk.CTkLabel(itutviklerutdanningframe, text="Første år: Informasjonsteknologi Og medieproduksjon",fg_color="orange",corner_radius=10)
itutviklerutdanningandreår = ctk.CTkLabel(itutviklerutdanningframe, text="Andre År: Informasjonsteknologi",fg_color="orange",corner_radius=10)
itutviklerutdanningtredjeogfjerdeår = ctk.CTkLabel(itutviklerutdanningframe, text="Tredje og fjerde år: IT-utviklerfaget",fg_color="green",corner_radius=10)

itumo = """
IT-utvikleren jobber med å utvikle og integrere IT-løsninger i en virksomhet. Arbeidsoppgavene består blant annet av:
Koding og programmering
Utvikle og designe IT-løsninger som er universelt
Utformet og tilpasset brukerens behov
Planlegge og vurdere virksomhetens bruk av ny
Teknologi og IT-løsninger
Vurdere og iverksette informasjonssikkerhet og
Personvern
Etikk og lovverk
"""
itutviklermuligeoppgaverframe = ctk.CTkFrame(root,corner_radius=10)

ututviklermuligeoppgaverbiglabel = ctk.CTkLabel(itutviklermuligeoppgaverframe, text="Mulige Oppgaver", font=("Arial", 20))
itutviklermuligeoppgaverlabel = ctk.CTkLabel(itutviklermuligeoppgaverframe, text=itumo, justify="left",font=("Arial", 15))

itutviklerpersonligeegenskaper = """
Du bør være systematisk, nøyaktig og løsningsorientert. Du må
kunne arbeide både selvstendig og i samarbeid med andre. Du bør 
være interessert i ny teknologi, ha evne til å tenke nytt og være
kretiv.
"""

itutviklerpersonligeegenskaperframe = ctk.CTkFrame(root,corner_radius=10)

itutviklerpersonligeegenskaperlabel = ctk.CTkLabel(itutviklerpersonligeegenskaperframe, text="Personlige Egenskaper", font=("Arial", 20))
itutviklerpersonligeegenskaper = ctk.CTkLabel(itutviklerpersonligeegenskaperframe, text=itutviklerpersonligeegenskaper, justify="left",font=("Arial", 15))

itutvikleraktueltarbeidssted = """
En IT-utvikler kan jobbe med IT-utvikling i alle typer virksomheter, offentlige og private.
"""
itutvikleraktueltarbeidsstedframe = ctk.CTkFrame(root,corner_radius=10)
itutvikleraktueltarbeidsstedlabel = ctk.CTkLabel(itutvikleraktueltarbeidsstedframe, text="Aktuelt Arbeidssted", font=("Arial", 20))
itutvikleraktueltarbeidssted = ctk.CTkLabel(itutvikleraktueltarbeidsstedframe, text=itutvikleraktueltarbeidssted, justify="left",font=("Arial", 15))

medieproduksjonsjobberframe = ctk.CTkFrame(root,corner_radius=10)

innholdsprodusentbutton = ctk.CTkButton(medieproduksjonsjobberframe, text="Innholdsprodusent", command=innholdsprodusentpage, hover_color="green")



innholdsprodusentframe = ctk.CTkFrame(root,corner_radius=10)

innholdsprodusentnødvendigutdanning = ctk.CTkLabel(innholdsprodusentframe, text="Nødvendig Utdanning", font=("Arial", 20))
innholdsprodusentførsteår = ctk.CTkLabel(innholdsprodusentframe, text="Første år: Informasjonsteknologi Og medieproduksjon",fg_color="orange",corner_radius=10)
innholdsprodusentandreår = ctk.CTkLabel(innholdsprodusentframe, text="Andre År: Medieproduksjon",fg_color="orange",corner_radius=10)
innholdsprodusenttredjeår = ctk.CTkLabel(innholdsprodusentframe, text="Tredje og fjerde år: innholdsproduksjonsfaget",fg_color="green",corner_radius=10)


innholdsprodusentmuligeoppgaver = """
Innholdsprodusenten jobber med kommunikasjon og utforming av innhold i ulike digitale kanaler. Arbeidsoppgavene består blant annet av:
• idéutvilkling
• planlegge, utvikle og produsere medieinnhold
• ta bilder og produsere video- og lydopptak
• analysere og forstå ulike kommunikasjonsbehov
• bruke ulike kommunikasjonskanaler og plattformer for publisering av innhold
• jobbe prosjektbasert og samarbeide med oppdragsgivere
"""
innholdsprodusentmuligeoppgaverframe = ctk.CTkFrame(root,corner_radius=10)
innholdsprodusentmuligeoppgaverlabel = ctk.CTkLabel(innholdsprodusentmuligeoppgaverframe, text="Mulige Oppgaver", font=("Arial", 20))
innholdsprodusentmuligeoppgaver = ctk.CTkLabel(innholdsprodusentmuligeoppgaverframe, text=innholdsprodusentmuligeoppgaver, justify="left",font=("Arial", 15))

innholdsprodusentPE = """
Du bør være interessert i kommunikasjon, teknologi, utstyr og programvare. Du
må ha gode samarbeidsevner, være kreativ og ha evne til å tenke nytt.
"""
innholdsprodusentPEframe = ctk.CTkFrame(root,corner_radius=10)
innholdsprodusentPElabel = ctk.CTkLabel(innholdsprodusentPEframe, text="Personlige Egenskaper", font=("Arial", 20))
innholdsprodusentPE = ctk.CTkLabel(innholdsprodusentPEframe, text=innholdsprodusentPE, justify="left",font=("Arial", 15))

innholdsprodusentaktueltarbeidssted = """
Du kan få arbeid i reklame-, design- og mediebyråer, forlag, aviser, grafisk
bransje, film- og TV-bransjen, og innen informasjonsvirksomhet i privat og
offentlig sektor.
"""

innholdsprodusentaktueltarbeidsstedframe = ctk.CTkFrame(root,corner_radius=10)
innholdsprodusentaktueltarbeidsstedlabel = ctk.CTkLabel(innholdsprodusentaktueltarbeidsstedframe, text="Aktuelt Arbeidssted", font=("Arial", 20))
innholdsprodusentaktueltarbeidssted = ctk.CTkLabel(innholdsprodusentaktueltarbeidsstedframe, text=innholdsprodusentaktueltarbeidssted, justify="left",font=("Arial", 15))

mediedesignernødvendigutdanningframe = ctk.CTkFrame(root,corner_radius=10)
mediedesignernødvendigutdanninglabel = ctk.CTkLabel(mediedesignernødvendigutdanningframe, text="Nødvendig Utdanning", font=("Arial", 20))
mediedesignernødvendigutdanningførsteår = ctk.CTkLabel(mediedesignernødvendigutdanningframe, text="Første år: Informasjonsteknologi Og medieproduksjon",fg_color="green",corner_radius=10)
mediedesignernødvendigutdanningandreår = ctk.CTkLabel(mediedesignernødvendigutdanningframe, text="Andre År: Medieproduksjon",fg_color="green",corner_radius=10)
mediedesingernødvendigutdanningtredjeår = ctk.CTkLabel(mediedesignernødvendigutdanningframe, text="Tredje og fjerde år: Mediedesignfaget",fg_color="orange",corner_radius=10)

mediedesignermuligeoppgaverTEXT = """
Mediedesigneren jobber med visuell kommunikasjon og design av medierelaterte produkter.
Arbeidsoppgavene består blant annet av:

konsept- og idéutvikling
design og produksjon av tekst, bilde og lyd for ulike publiseringsløsninger og for ulike målgrupper
bruke virkemidler og ulike teknikker i design av produkter eller brukeropplevelser
arbeide med formspråk og visuelle virkemidler
bruk av utstyr og programvare
"""
mediedesignermuligeoppgaverframe = ctk.CTkFrame(root,corner_radius=10)
mediedesignermuligeoppgaverlabel = ctk.CTkLabel(mediedesignermuligeoppgaverframe, text="Mulige Oppgaver", font=("Arial", 20))
mediedesignermuligeoppgaver = ctk.CTkLabel(mediedesignermuligeoppgaverframe, text=mediedesignermuligeoppgaverTEXT, justify="left",font=("Arial", 15))

mediedesignerperonligeegenskaperTEXT = """
Du bør være interessert i visuell kommunikasjon, design og
teknologiske løsninger. Du bør være kreativ, nysgjerrig og ha
problemløsende evner. Det er viktig at du kan arbeide både
selvstendig og i team.
"""

mediedesignerpersonligeegenskaperframe = ctk.CTkFrame(root,corner_radius=10)
mediedesignerperonligeegenskaperlabel = ctk.CTkLabel(mediedesignerpersonligeegenskaperframe, text="Personlige Egenskaper", font=("Arial", 20))
mediedesignerpersonligeegenskaper = ctk.CTkLabel(mediedesignerpersonligeegenskaperframe, text=mediedesignerperonligeegenskaperTEXT, justify="left",font=("Arial", 15))

mediedesigneraktueltarbeidsstedTEXT = """
En mediedesigner kan jobbe innen medie- og
kommunikasjonssektoren, i reklame-, design- og mediebyråer,
forlag, aviser, grafisk bransje, film og TV-bransjen, og innen
informasjonsvirksomhet i privat og offentlig sektor.
"""

mediedesigneraktueltarbeidsstedframe = ctk.CTkFrame(root,corner_radius=10)
mediedesigneraktueltarbeidsstedlabel = ctk.CTkLabel(mediedesigneraktueltarbeidsstedframe, text="Aktuelt Arbeidssted", font=("Arial", 20))
mediedesigneraktueltarbeidssted = ctk.CTkLabel(mediedesigneraktueltarbeidsstedframe, text=mediedesigneraktueltarbeidsstedTEXT, justify="left",font=("Arial", 15))

medieteknikernødvendigutdanningframe = ctk.CTkFrame(root,corner_radius=10)
medieteknikernødvendigutdanninglabel = ctk.CTkLabel(medieteknikernødvendigutdanningframe, text="Nødvendig Utdanning", font=("Arial", 20))
medieteknikernødvendigutdanningførsteår = ctk.CTkLabel(medieteknikernødvendigutdanningframe, text="Første år: Informasjonsteknologi Og medieproduksjon",fg_color="green",corner_radius=10)
medieteknikernødvendigutdanningandreår = ctk.CTkLabel(medieteknikernødvendigutdanningframe, text="Andre År: Medieproduksjon",fg_color="green",corner_radius=10)
medieteknikernødvendigutdanningtredjeår = ctk.CTkLabel(medieteknikernødvendigutdanningframe, text="Tredje og fjerde år: Medieteknikkfaget",fg_color="orange",corner_radius=10)

medieteknikermuligeoppgaverTEXT = """
Medieteknikeren jobber med audiovisuelt innhold og utstyr i alle typer medieproduksjoner. Arbeidsoppgavene består blant annet av:
ha ansvar for utstyr i film- og tv produksjoner, konferanser og kulturarrangementer
vedlikeholde og drifte teknisk utstyr
arbeide med flerkameraproduksjon
organisere og sette opp gode tekniske løsninger
i medieproduksjoner og i audiovisuelle installasjoner
"""

medieteknikermuligeoppgaverframe = ctk.CTkFrame(root,corner_radius=10)
medieteknikermuligeoppgaverlabel = ctk.CTkLabel(medieteknikermuligeoppgaverframe, text="Mulige Oppgaver", font=("Arial", 20))
medieteknikermuligeoppgaver = ctk.CTkLabel(medieteknikermuligeoppgaverframe, text=medieteknikermuligeoppgaverTEXT, justify="left",font=("Arial", 15))

medieteknikerpersonligegenkaperTEXT = """
Du bør være interessert i medieproduksjon, teknisk utstyr og IT. Det
er viktig å kunne kommunisere godt og være løsningsorientert, og du
må kunne jobbe selvstendig og ha gode samarbeids evner.
"""

medieteknikerpersonligeegenskaperframe = ctk.CTkFrame(root,corner_radius=10)
medieteknikerpersonligeegenskaperlabel = ctk.CTkLabel(medieteknikerpersonligeegenskaperframe, text="Personlige Egenskaper", font=("Arial", 20))
medieteknikerpersonligeegenskaper = ctk.CTkLabel(medieteknikerpersonligeegenskaperframe, text=medieteknikerpersonligegenkaperTEXT, justify="left",font=("Arial", 15))

medieteknikeraktueltarbeidsstedTEXT = """
En medietekniker kan jobbe innen medie- og
kommunikasjonssektoren, i reklamebransjen og i film- og TV-
bransjen, og innen informasjonsvirksomhet i privat og offentlig sektor.
"""

medieteknikeraktueltarbeidsstedframe = ctk.CTkFrame(root,corner_radius=10)
medieteknikeraktueltarbeidsstedlabel = ctk.CTkLabel(medieteknikeraktueltarbeidsstedframe, text="Aktuelt Arbeidssted", font=("Arial", 20))
medieteknikeraktueltarbeidssted = ctk.CTkLabel(medieteknikeraktueltarbeidsstedframe, text=medieteknikeraktueltarbeidsstedTEXT, justify="left",font=("Arial", 15))

fagfordelingoptions1 = ["InformasjonsTeknologi og Medieproduksjon"]


fagfordelingchoiceframe = ctk.CTkFrame(root,corner_radius=10)

showmainpage()
root.mainloop()