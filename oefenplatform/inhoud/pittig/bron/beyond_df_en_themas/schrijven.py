"""Schrijven, spreken en literatuurbeleving — pittig (Engels, Beyond dubbele finaliteit), A2+."""
from ..beyond_en_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Read Noah's email.\n\n« Dear Mrs Clark,\n\nI saw your advert for a babysitter on the school website. I am seventeen and I often look after my little brothers. "
        "I am free on Wednesday afternoons and at the weekend. Could you tell me how much you pay per hour?\n\n"
        "I look forward to hearing from you.\n\nYours sincerely,\nNoah Peeters »",
        [
            keuze("Het register van deze mail is [[*formeel|informeel]].", "Dear Mrs Clark en Yours sincerely."),
            keuze("Noah sluit af met « Yours sincerely » omdat hij [[*de naam van de lezer kent|de lezer niet kent]].",
                  "Bij een bekende naam: Yours sincerely."),
            mk("Wat vraagt Noah aan Mrs Clark?",
               ["hoeveel ze per uur betaalt", "of hij op woensdag mag beginnen", "hoe oud haar kinderen zijn", "waar ze precies woont"], 0,
               "Could you tell me how much you pay per hour?"),
            keuze("« Could you tell me ... » is een [[*hoffelijke|onbeleefde]] manier om iets te vragen.", "Could you is beleefd."),
            mk("Welke zin hoort bij het slot van de mail?",
               ["I look forward to hearing from you.", "I saw your advert on the school website.", "I am seventeen and look after my brothers.", "I am free on Wednesday afternoons."], 0,
               "Een slotzin kijkt uit naar een antwoord."),
        ],
    ),
    tabel("Is dit een goede strategie bij een schrijfopdracht?", [
        ("eerst een lijstje kernwoorden maken", J), ("de opgegeven lengte negeren", F),
        ("je tekst nalezen voor je hem inlevert", J), ("alles in één lange alinea zetten", F),
    ], "Plannen, de lengte respecteren, alinea's maken en nalezen."),
    volgorde("Zet de stappen van een schrijfopdracht in de juiste volgorde.", [
        "nadenken waarom en voor wie je schrijft", "een lijstje kernwoorden maken", "de tekst schrijven", "de tekst nalezen",
    ], "Eerst het communicatiemodel, dan plannen, schrijven en nalezen."),
    sorteer("Hoort het bij een formele of een informele mail?", ["formeel", "informeel"], [
        ["Dear Sir or Madam,", "formeel"], ["Hi Tom,", "informeel"], ["Yours faithfully,", "formeel"],
        ["Love,", "informeel"], ["Thank you in advance.", "formeel"], ["Cheers!", "informeel"],
    ], "Formeel tegenover een onbekende, informeel tegenover een vriend."),
    koppel("Koppel elk woord over verhalen aan zijn betekenis.", [
        ["the plot", "de verhaallijn"], ["the setting", "de plaats en de tijd"], ["the main character", "het hoofdpersonage"], ["the narrator", "de verteller"],
    ], ["de dichter"], "A poet is de dichter."),
    koppel("Koppel elke zin aan wat je ermee doet.", [
        ["Could you tell me the way to the station?", "informatie vragen"], ["You should try it, it's cheaper.", "overtuigen"],
        ["For example, you can take the bus.", "iets uitleggen"], ["I liked it because it was funny.", "een mening geven"],
    ], ["iemand bedanken"], "Elke zin heeft een eigen doel."),
    mk("Je mail aan een onbekende begint met « Dear Sir or Madam, ». Hoe sluit je af?",
       ["Yours faithfully,", "Yours sincerely, with love", "See you soon, bye,", "Lots of love and kisses,"], 0,
       "Na Dear Sir or Madam: Yours faithfully."),
    mk("Je verstaat je gesprekspartner niet goed. Wat zeg je?",
       ["Could you speak more slowly, please?", "I don't care at all what you are saying.", "Stop talking to me now, please, thank you.", "You speak very bad English, I think."], 0,
       "Vraag beleefd om trager te spreken."),
    mk("Je kent het Engelse woord voor « ladder » niet. Wat doe je in je tekst?",
       ["het omschrijven met woorden die je wel kent", "het Nederlandse woord gewoon in de zin laten staan", "de hele zin dan maar uit de tekst weglaten", "stoppen met schrijven en iets anders doen"], 0,
       "Bereik je doel met wat je al kent."),
    mk("Welke zin geeft je eigen beleving bij een verhaal?",
       ["The ending made me feel sad, because the dog died.", "The story has twelve chapters and a big map at the back.", "The writer of this story was born in Dublin in 1960.", "The book was printed in London by a big company."], 0,
       "Beleving: wat de tekst bij jou doet, met een reden."),
    mk("Je vriend vraagt of hij het boek moet lezen. Welke zin overtuigt?",
       ["You should read it, it's really exciting.", "The book has exactly 200 pages in total.", "The book costs ten pounds at the bookshop.", "Is the book also in the school library?"], 0,
       "Een aanbeveling met een argument."),
    mk("Welke van deze zinnen is een vraag om informatie?",
       ["What time does the shop open?", "The shop opens at nine every day.", "I think the shop is really great.", "Go to the shop now, it is open."], 0,
       "Een vraag naar het uur."),
    inv("Vul in: « Could you ___ that, please? » Je vraagt om iets nog eens te zeggen. Eén woord.", ["repeat"],
        "Could you repeat that, please?"),
    inv("Hoe zeg je dichter in het Engels? Eén woord.", ["poet", "a poet"], "A poem, a poet."),
    inv("Hoe zeg je recensie in het Engels? Eén woord.", ["review", "a review"], "A review."),
    inv("Hoe zeg je samenvatting in het Engels? Eén woord.", ["summary", "a summary"], "A summary."),
    keuze("Bij een uitleg zeg je « [[*for example|for nothing]] » om een voorbeeld te geven.", "For example of for instance."),
    keuze("Spelfouten mogen bij het examen [[*het tekstbegrip niet in de weg staan|nooit voorkomen]].", "Foutloos hoeft niet, duidelijk wel."),
    keuze("Een tekst verdeel je in [[*alinea's|zinnen zonder witregel]] met een witregel ertussen.", "Eén gedachte per alinea."),
    keuze("Bij een spreekopdracht tellen [[*je uitspraak en je lichaamstaal|alleen je woorden]] mee.", "Ook spreektempo en intonatie."),
    keuze("Bij literatuurbeleving [[*mag|mag niet]] je zeggen dat een verhaal je niet aanspreekt, als je uitlegt waarom.",
          "Het gaat om jouw beleving."),
    tabel("Is dit een goede zin om een vriend te overtuigen om mee te gaan kamperen?", [
        ("It's cheap and we can swim in the lake.", J), ("What is your address?", F),
        ("You should come, it will be fun!", J), ("The campsite has a website.", F),
    ], "Overtuigen: een argument of een aanbeveling geven."),
    sleep("Hi Emma,\n\nThanks [[for]] your message! I am going [[to]] London next week. [[Could]] you send me the address of your hotel?\n\nLove, Mia",
          ["of", "Must"], "Thanks for, going to, could you."),
    open_("Je las een kortverhaal over een jongen die zijn hond verliest. Schrijf in het Engels één zin over wat het verhaal bij jou deed, met een reden.",
          "I felt sad when he lost his dog, because I have a dog too.",
          "Een gevoel plus because met een reden."),
    inv("Hoe zeg je alinea in het Engels? Eén woord.", ["paragraph", "a paragraph"], "A paragraph."),
    tabel("Hoort dit bij een goede tekststructuur?", [
        ("een inleiding, een midden en een slot", J), ("signaalwoorden zoals first en finally", J), ("geen titel en geen alinea's", F),
    ], "Inleiding, midden en slot met duidelijke tekstverbanden."),
]
