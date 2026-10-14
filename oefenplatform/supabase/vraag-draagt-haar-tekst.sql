-- De vragen die naar een tekst van een vorige vraag verwezen, dragen die
-- tekst nu zelf. Door Kim gemeld op 14 oktober 2026: op het examen stond
-- "Dezelfde tekst over de schoolyard. Welke hoofdpunten staan erin?" zonder
-- dat die tekst ergens te zien was, want op een examen lopen de vragen van
-- alle hoofdstukken door elkaar.
--
-- 116 vragen uit zes vakken: Engels en Frans van Spark, Boost doorstroom en
-- Boost dubbele finaliteit. Dit vervangt een herimport van die zes bestanden;
-- de bronbestanden in de repo zijn mee aangepast.
--
-- Draai dit in de sql-editor van Supabase, op het project van het
-- oefenplatform. Onderaan komt er een getal uit: dat hoort 116 te zijn.

-- spark/engels.json | Een Engelse tekst lezen — deel 1
update vragen set vraag = $v$Lees nog eens: 'Our school has a new bike shed. Students can park their bikes there for free. The shed is open from 8 a.m. until 5 p.m.' Welke zinnen zijn HOOFDPUNTEN, die de hoofdgedachte ondersteunen?$v$
 where vraag = $v$Nog eens die tekst over de bike shed. Welke zinnen zijn HOOFDPUNTEN, die de hoofdgedachte ondersteunen?$v$;

-- spark/engels.json | Een Engelse tekst lezen — deel 1
update vragen set vraag = $v$Lees nog eens: 'I loved the new Spider-Man film. The actors are great and the costumes look amazing. The story is a bit slow, but I still had a good time.' Welke hoofdpunten geeft de schrijver?$v$
 where vraag = $v$Dezelfde review over Spider-Man. Welke hoofdpunten geeft de schrijver?$v$;

-- spark/engels.json | Een Engelse tekst lezen — deel 1
update vragen set vraag = $v$Lees nog eens: 'The school trip to London costs 180 euros. Please pay before 15 March. The bus leaves at 6 a.m.' In die tekst over de schoolreis moet je betalen vóór 15 maart.$v$
 where vraag = $v$In die tekst over de schoolreis moet je betalen vóór 15 maart.$v$;

-- spark/engels.json | Een Engelse tekst lezen — deel 2
update vragen set vraag = $v$Lees nog eens: 'Every Friday our class cleans the schoolyard. We pick up paper and plastic. Last week we filled six bags.' Welke hoofdpunten staan erin?$v$
 where vraag = $v$Dezelfde tekst over de schoolyard. Welke hoofdpunten staan erin?$v$;

-- spark/engels.json | Een Engelse tekst lezen — deel 2
update vragen set vraag = $v$Lees nog eens: 'Hi Sam, sorry, I can't come to your party. I have to visit my grandmother. Have fun! Lucy' In dat bericht verontschuldigt Lucy zich.$v$
 where vraag = $v$In dat bericht verontschuldigt Lucy zich.$v$;

-- spark/engels.json | Een Engelse tekst lezen — deel 2
update vragen set vraag = $v$Lees nog eens: 'The museum is closed on Mondays, but the garden stays open.' In die tekst over het museum is de tuin op maandag ook gesloten.$v$
 where vraag = $v$In die tekst over het museum is de tuin op maandag ook gesloten.$v$;

-- spark/engels.json | Een Engelse tekst lezen — deel 2
update vragen set vraag = $v$Lees nog eens: 'We arrived in Scotland on Monday. It rained all week, but the mountains were beautiful.' In die blog over Schotland regende het de hele week.$v$
 where vraag = $v$In die blog over Schotland regende het de hele week.$v$;

-- spark/engels.json | Tekstsoorten, signaalwoorden en verwijswoorden — deel 2
update vragen set vraag = $v$Lees nog eens: 'Our town needs a new swimming pool. The old one is too small and it is often closed.' Welke argumenten geeft de schrijver?$v$
 where vraag = $v$Dezelfde tekst over het zwembad. Welke argumenten geeft de schrijver?$v$;

-- spark/engels.json | Tekstsoorten, signaalwoorden en verwijswoorden — deel 2
update vragen set vraag = $v$Je ziet een Engelse cartoon: één tekening van een jongen die nog in bed ligt, met eronder 'Monday again? My bed disagrees.' Bij welke soort teksten hoort zo'n cartoon?$v$, uitleg = $v$Monday again? My bed disagrees = alweer maandag? Mijn bed is het daar niet mee eens. Zo'n grapje wil je laten lachen, niet informeren of iets opdragen. De fiche noemt een lied, een gedicht, een cartoon, een strip en een kortverhaal bij de literaire teksten. Een narratieve tekst vertelt een verhaal dat vooruitgaat in de tijd, en één tekening met één zin doet dat niet.$v$
 where vraag = $v$Je leest een cartoon met één tekening en één zin eronder. Bij welke soort teksten hoort dat?$v$;

-- spark/engels.json | Engelstalige landen en literaire teksten — deel 2
update vragen set vraag = $v$Lees nog eens: 'The rain keeps falling on the empty street. / Nobody waits for me tonight.' Je moet schriftelijk reageren op dat gedicht over de regen. Welke reacties passen bij wat de fiche vraagt?$v$
 where vraag = $v$Je moet schriftelijk reageren op dat gedicht over de regen. Welke reacties passen bij wat de fiche vraagt?$v$;

-- spark/frans.json | Een Franse tekst lezen — deel 2
update vragen set vraag = $v$Lees nog eens: 'Les jeunes passent trop de temps devant leur écran. Ils dorment moins bien et bougent moins.' Welke zinnen uit die tekst zijn hoofdpunten die de hoofdgedachte ondersteunen?$v$
 where vraag = $v$Welke zinnen uit die tekst zijn hoofdpunten die de hoofdgedachte ondersteunen?$v$;

-- boost-doorstroom/engels.json | Een Engelse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Every spring, thousands of swifts arrive in Belgium after a journey of more than six thousand kilometres. They nest under roof tiles and in wall cavities. Because many old buildings are being renovated, those nesting places are disappearing fast. Several cities now require builders to put nest bricks into the walls of new houses.' Wat is de HOOFDGEDACHTE?$v$
 where vraag = $v$Dezelfde tekst over de swifts. Wat is de HOOFDGEDACHTE?$v$;

-- boost-doorstroom/engels.json | Een Engelse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Every spring, thousands of swifts arrive in Belgium after a journey of more than six thousand kilometres. They nest under roof tiles and in wall cavities. Because many old buildings are being renovated, those nesting places are disappearing fast. Several cities now require builders to put nest bricks into the walls of new houses.' Welke zinnen uit de tekst over de swifts zijn HOOFDPUNTEN?$v$
 where vraag = $v$Welke zinnen uit de tekst over de swifts zijn HOOFDPUNTEN?$v$;

-- boost-doorstroom/engels.json | Een Engelse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Every spring, thousands of swifts arrive in Belgium after a journey of more than six thousand kilometres. They nest under roof tiles and in wall cavities. Because many old buildings are being renovated, those nesting places are disappearing fast. Several cities now require builders to put nest bricks into the walls of new houses.' Hoeveel kilometer vliegen de swifts volgens de tekst? Antwoord met een getal.$v$
 where vraag = $v$Hoeveel kilometer vliegen de swifts volgens de tekst? Antwoord met een getal.$v$;

-- boost-doorstroom/engels.json | Een Engelse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'We stayed at the Riverside Hotel for three nights. The rooms were clean and the staff could not have been friendlier. Breakfast, however, was disappointing: cold coffee and very little choice. For this price I would expect more.' Welke woorden in de hotelbeoordeling dragen het negatieve oordeel?$v$
 where vraag = $v$Welke woorden in de hotelbeoordeling dragen het negatieve oordeel?$v$;

-- boost-doorstroom/engels.json | Een Engelse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'On our third day in Wales the rain finally stopped. We walked along the coast for six hours and met nobody except a farmer and about two hundred sheep. By the evening my legs hurt, but I would do it again tomorrow.' Hoeveel uur wandelden ze volgens het reisverslag? Antwoord met een getal.$v$
 where vraag = $v$Hoeveel uur wandelden ze volgens het reisverslag? Antwoord met een getal.$v$;

-- boost-doorstroom/engels.json | Een Engelse tekst analyseren — deel 2
update vragen set vraag = $v$Lees nog eens: 'Before you start, read all the steps. Preheat the oven to 180 °C. Mix the flour, the sugar and the eggs in a large bowl. Do not add the butter until the mixture is smooth. Bake for 25 minutes and let the cake cool before you cut it.' Welke aanwijzingen in het recept zijn imperatieven?$v$
 where vraag = $v$Welke aanwijzingen in het recept zijn imperatieven?$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Depuis trois ans, la ville de Namur prête des vélos électriques aux habitants qui travaillent à plus de cinq kilomètres de chez eux. Le prêt dure six semaines et ne coûte rien. L'idée n'est pas de donner un vélo à tout le monde, mais de laisser les gens essayer. Après l'essai, un habitant sur trois achète son propre vélo.' Wat is de hoofdgedachte, dus de belangrijkste boodschap?$v$
 where vraag = $v$Hetzelfde tekstje over Namen. Wat is de hoofdgedachte, dus de belangrijkste boodschap?$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Depuis trois ans, la ville de Namur prête des vélos électriques aux habitants qui travaillent à plus de cinq kilomètres de chez eux. Le prêt dure six semaines et ne coûte rien. L'idée n'est pas de donner un vélo à tout le monde, mais de laisser les gens essayer. Après l'essai, un habitant sur trois achète son propre vélo.' Hoeveel weken mag je de fiets houden? Schrijf het cijfer.$v$
 where vraag = $v$Nog altijd het tekstje over Namen. Hoeveel weken mag je de fiets houden? Schrijf het cijfer.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Depuis trois ans, la ville de Namur prête des vélos électriques aux habitants qui travaillent à plus de cinq kilomètres de chez eux. Le prêt dure six semaines et ne coûte rien. L'idée n'est pas de donner un vélo à tout le monde, mais de laisser les gens essayer. Après l'essai, un habitant sur trois achète son propre vélo.' In het tekstje over Namen kost het niets om de fiets zes weken te mogen proberen.$v$
 where vraag = $v$In het tekstje over Namen kost het niets om de fiets zes weken te mogen proberen.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Depuis trois ans, la ville de Namur prête des vélos électriques aux habitants qui travaillent à plus de cinq kilomètres de chez eux. Le prêt dure six semaines et ne coûte rien. L'idée n'est pas de donner un vélo à tout le monde, mais de laisser les gens essayer. Après l'essai, un habitant sur trois achète son propre vélo.' Welke dingen staan er letterlijk in het tekstje over Namen?$v$
 where vraag = $v$Welke dingen staan er letterlijk in het tekstje over Namen?$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Notre école a changé le menu de la cantine en septembre. Il y a maintenant un plat végétarien tous les jours et moins de viande. Au début, beaucoup d'élèves se sont plaints. Trois mois plus tard, la cantine sert deux fois plus de repas qu'avant. Le cuisinier explique que le secret n'est pas le menu, mais le goût.' Wat is de hoofdgedachte?$v$
 where vraag = $v$Hetzelfde tekstje over de kantine. Wat is de hoofdgedachte?$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Notre école a changé le menu de la cantine en septembre. Il y a maintenant un plat végétarien tous les jours et moins de viande. Au début, beaucoup d'élèves se sont plaints. Trois mois plus tard, la cantine sert deux fois plus de repas qu'avant. Le cuisinier explique que le secret n'est pas le menu, mais le goût.' In het tekstje over de kantine waren de leerlingen vanaf het begin tevreden.$v$
 where vraag = $v$In het tekstje over de kantine waren de leerlingen vanaf het begin tevreden.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Notre école a changé le menu de la cantine en septembre. Il y a maintenant un plat végétarien tous les jours et moins de viande. Au début, beaucoup d'élèves se sont plaints. Trois mois plus tard, la cantine sert deux fois plus de repas qu'avant. Le cuisinier explique que le secret n'est pas le menu, mais le goût.' Hoeveel maanden later serveert de kantine dubbel zoveel maaltijden? Schrijf het cijfer.$v$
 where vraag = $v$Nog het tekstje over de kantine. Hoeveel maanden later serveert de kantine dubbel zoveel maaltijden? Schrijf het cijfer.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Hier soir, un orage violent a traversé le sud du pays. Plusieurs routes ont été fermées pendant deux heures. Il n'y a pas de blessés, mais une centaine de maisons sont restées sans électricité jusqu'à ce matin.' Welke gevolgen van dat onweer worden in het bericht genoemd?$v$
 where vraag = $v$Welke gevolgen van dat onweer worden in het bericht genoemd?$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Hier soir, un orage violent a traversé le sud du pays. Plusieurs routes ont été fermées pendant deux heures. Il n'y a pas de blessés, mais une centaine de maisons sont restées sans électricité jusqu'à ce matin.' In het nieuwsbericht over het onweer vielen er gewonden.$v$
 where vraag = $v$In het nieuwsbericht over het onweer vielen er gewonden.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Hier soir, un orage violent a traversé le sud du pays. Plusieurs routes ont été fermées pendant deux heures. Il n'y a pas de blessés, mais une centaine de maisons sont restées sans électricité jusqu'à ce matin.' Hoeveel huizen zaten er volgens het nieuwsbericht ongeveer zonder stroom? Antwoord in cijfers.$v$
 where vraag = $v$Hoeveel huizen zaten er volgens het nieuwsbericht ongeveer zonder stroom? Antwoord in cijfers.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Madame, Monsieur, Je suis élève en quatrième année et je cherche un stage de deux semaines au mois de février. Je m'intéresse beaucoup au travail de votre laboratoire. Je suis libre tous les jours et je peux venir me présenter quand vous voulez. Je vous remercie d'avance pour votre réponse.' De schrijver van die brief laat weten wanneer hij of zij beschikbaar is.$v$
 where vraag = $v$De schrijver van die brief laat weten wanneer hij of zij beschikbaar is.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Madame, Monsieur, Je suis élève en quatrième année et je cherche un stage de deux semaines au mois de février. Je m'intéresse beaucoup au travail de votre laboratoire. Je suis libre tous les jours et je peux venir me présenter quand vous voulez. Je vous remercie d'avance pour votre réponse.' In welke maand wil de schrijver van die brief stage lopen?$v$
 where vraag = $v$In welke maand wil de schrijver van die brief stage lopen?$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Le samedi matin, la place est pleine. On y vend des légumes, du fromage et des fleurs. Les prix sont plus élevés qu'au supermarché, mais les clients reviennent chaque semaine. « Ici, je sais qui a cultivé mes tomates », dit une dame de soixante ans.' Op de markt uit dat tekstje liggen de prijzen hoger dan in de supermarkt.$v$
 where vraag = $v$Op de markt uit dat tekstje liggen de prijzen hoger dan in de supermarkt.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 2
update vragen set vraag = $v$Lees nog eens: 'Depuis trois ans, la ville de Namur prête des vélos électriques aux habitants qui travaillent à plus de cinq kilomètres de chez eux. Le prêt dure six semaines et ne coûte rien. L'idée n'est pas de donner un vélo à tout le monde, mais de laisser les gens essayer. Après l'essai, un habitant sur trois achète son propre vélo.' Uit het tekstje over Namen kan je afleiden dat twee op de drie inwoners na de proef geen eigen fiets kopen.$v$
 where vraag = $v$Uit het tekstje over Namen kan je afleiden dat twee op de drie inwoners na de proef geen eigen fiets kopen.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 2
update vragen set vraag = $v$Lees nog eens: 'Notre école a changé le menu de la cantine en septembre. Il y a maintenant un plat végétarien tous les jours et moins de viande. Au début, beaucoup d'élèves se sont plaints. Trois mois plus tard, la cantine sert deux fois plus de repas qu'avant. Le cuisinier explique que le secret n'est pas le menu, mais le goût.' Welke woorden in het tekstje over de kantine wijzen op een tijdsverloop?$v$
 where vraag = $v$Welke woorden in het tekstje over de kantine wijzen op een tijdsverloop?$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 2
update vragen set vraag = $v$Lees nog eens: 'Notre école a changé le menu de la cantine en septembre. Il y a maintenant un plat végétarien tous les jours et moins de viande. Au début, beaucoup d'élèves se sont plaints. Trois mois plus tard, la cantine sert deux fois plus de repas qu'avant. Le cuisinier explique que le secret n'est pas le menu, mais le goût.' In het tekstje over de kantine is het een leerling die uitlegt waarom het nu wel lukt.$v$
 where vraag = $v$In het tekstje over de kantine is het een leerling die uitlegt waarom het nu wel lukt.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 2
update vragen set vraag = $v$Lees nog eens: 'Madame, Monsieur, Je suis élève en quatrième année et je cherche un stage de deux semaines au mois de février. Je m'intéresse beaucoup au travail de votre laboratoire. Je suis libre tous les jours et je peux venir me présenter quand vous voulez. Je vous remercie d'avance pour votre réponse.' Welke zinnen uit die stagebrief zijn beleefdheidsformules?$v$
 where vraag = $v$Welke zinnen uit die stagebrief zijn beleefdheidsformules?$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 2
update vragen set vraag = $v$Lees nog eens: 'Madame, Monsieur, Je suis élève en quatrième année et je cherche un stage de deux semaines au mois de février. Je m'intéresse beaucoup au travail de votre laboratoire. Je suis libre tous les jours et je peux venir me présenter quand vous voulez. Je vous remercie d'avance pour votre réponse.' De schrijver van de stagebrief zegt waarom juist dat labo hem of haar interesseert.$v$
 where vraag = $v$De schrijver van de stagebrief zegt waarom juist dat labo hem of haar interesseert.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 2
update vragen set vraag = $v$Lees nog eens: 'Le samedi matin, la place est pleine. On y vend des légumes, du fromage et des fleurs. Les prix sont plus élevés qu'au supermarché, mais les clients reviennent chaque semaine. « Ici, je sais qui a cultivé mes tomates », dit une dame de soixante ans.' Uit het tekstje over de markt blijkt dat de dame van zestig haar tomaten zelf kweekt.$v$
 where vraag = $v$Uit het tekstje over de markt blijkt dat de dame van zestig haar tomaten zelf kweekt.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 2
update vragen set vraag = $v$Lees nog eens: 'Marie : J'ai acheté ce casque il y a deux mois et le son est déjà mauvais d'un côté. Quelqu'un a le même problème ? — Yacine : Chez moi, c'était le câble. Je l'ai remplacé pour douze euros et tout fonctionne. — Lila : Moi, j'ai renvoyé le mien. La garantie dure deux ans, profites-en.' Welke oplossingen stellen de anderen op dat forum voor?$v$
 where vraag = $v$Welke oplossingen stellen de anderen op dat forum voor?$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 2
update vragen set vraag = $v$Lees nog eens: 'Marie : J'ai acheté ce casque il y a deux mois et le son est déjà mauvais d'un côté. Quelqu'un a le même problème ? — Yacine : Chez moi, c'était le câble. Je l'ai remplacé pour douze euros et tout fonctionne. — Lila : Moi, j'ai renvoyé le mien. La garantie dure deux ans, profites-en.' Op dat forum heeft Yacine zijn koptelefoon teruggestuurd.$v$
 where vraag = $v$Op dat forum heeft Yacine zijn koptelefoon teruggestuurd.$v$;

-- boost-doorstroom/frans.json | Een Franse tekst analyseren — deel 2
update vragen set vraag = $v$Lees nog eens de twee tekstjes. Over de markt: 'Le samedi matin, la place est pleine. On y vend des légumes, du fromage et des fleurs. Les prix sont plus élevés qu'au supermarché, mais les clients reviennent chaque semaine. « Ici, je sais qui a cultivé mes tomates », dit une dame de soixante ans.' En het forum: 'Marie : J'ai acheté ce casque il y a deux mois et le son est déjà mauvais d'un côté. Quelqu'un a le même problème ? — Yacine : Chez moi, c'était le câble. Je l'ai remplacé pour douze euros et tout fonctionne. — Lila : Moi, j'ai renvoyé le mien. La garantie dure deux ans, profites-en.' Ze gaan allebei over kopen. Wat is het grootste verschil?$v$
 where vraag = $v$Het tekstje over de markt en het stukje forum gaan allebei over kopen. Wat is het grootste verschil?$v$;

-- boost-doorstroom/frans.json | Tekstsoorten, tekstverbanden en verwijswoorden — deel 1
update vragen set vraag = $v$Lees nog eens: 'Épluchez quatre pommes de terre et coupez-les en morceaux. Faites-les cuire vingt minutes dans l'eau bouillante. Égouttez, puis écrasez-les avec un peu de lait chaud. Salez et servez tout de suite.' Waaraan zie je in dat recept meteen dat het een prescriptieve tekst is?$v$
 where vraag = $v$Waaraan zie je in dat recept meteen dat het een prescriptieve tekst is?$v$;

-- boost-dubbele-finaliteit/engels.json | Een Engelse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Every spring, thousands of swifts arrive in Belgium after a journey of more than six thousand kilometres. They nest under roof tiles and in wall cavities. Because many old buildings are being renovated, those nesting places are disappearing fast. Several cities now require builders to put nest bricks into the walls of new houses.' Wat is de HOOFDGEDACHTE?$v$
 where vraag = $v$Dezelfde tekst over de swifts. Wat is de HOOFDGEDACHTE?$v$;

-- boost-dubbele-finaliteit/engels.json | Een Engelse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Every spring, thousands of swifts arrive in Belgium after a journey of more than six thousand kilometres. They nest under roof tiles and in wall cavities. Because many old buildings are being renovated, those nesting places are disappearing fast. Several cities now require builders to put nest bricks into the walls of new houses.' Welke zinnen uit de tekst over de swifts zijn HOOFDPUNTEN?$v$
 where vraag = $v$Welke zinnen uit de tekst over de swifts zijn HOOFDPUNTEN?$v$;

-- boost-dubbele-finaliteit/engels.json | Een Engelse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'Every spring, thousands of swifts arrive in Belgium after a journey of more than six thousand kilometres. They nest under roof tiles and in wall cavities. Because many old buildings are being renovated, those nesting places are disappearing fast. Several cities now require builders to put nest bricks into the walls of new houses.' Hoeveel kilometer vliegen de swifts volgens de tekst? Antwoord met een getal.$v$
 where vraag = $v$Hoeveel kilometer vliegen de swifts volgens de tekst? Antwoord met een getal.$v$;

-- boost-dubbele-finaliteit/engels.json | Een Engelse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'We stayed at the Riverside Hotel for three nights. The rooms were clean and the staff could not have been friendlier. Breakfast, however, was disappointing: cold coffee and very little choice. For this price I would expect more.' Welke woorden in de hotelbeoordeling dragen het negatieve oordeel?$v$
 where vraag = $v$Welke woorden in de hotelbeoordeling dragen het negatieve oordeel?$v$;

-- boost-dubbele-finaliteit/engels.json | Een Engelse tekst analyseren — deel 1
update vragen set vraag = $v$Lees nog eens: 'On our third day in Wales the rain finally stopped. We walked along the coast for six hours and met nobody except a farmer and about two hundred sheep. By the evening my legs hurt, but I would do it again tomorrow.' Hoeveel uur wandelden ze volgens het reisverslag? Antwoord met een getal.$v$
 where vraag = $v$Hoeveel uur wandelden ze volgens het reisverslag? Antwoord met een getal.$v$;

-- boost-dubbele-finaliteit/engels.json | Een Engelse tekst analyseren — deel 2
update vragen set vraag = $v$Lees nog eens: 'Before you start, read all the steps. Preheat the oven to 180 °C. Mix the flour, the sugar and the eggs in a large bowl. Do not add the butter until the mixture is smooth. Bake for 25 minutes and let the cake cool before you cut it.' Welke aanwijzingen in het recept zijn imperatieven?$v$
 where vraag = $v$Welke aanwijzingen in het recept zijn imperatieven?$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « À vendre : vélo de ville bleu, taille moyenne. Je l'ai acheté il y a deux ans et je roule très peu. Les pneus sont neufs. Prix : 95 euros. Je ne fais pas d'envoi : il faut venir le chercher à Liège, le samedi ou le dimanche. » Wat is de hoofdgedachte, dus de belangrijkste boodschap?$v$
 where vraag = $v$Hetzelfde zoekertje over de fiets. Wat is de hoofdgedachte, dus de belangrijkste boodschap?$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « À vendre : vélo de ville bleu, taille moyenne. Je l'ai acheté il y a deux ans et je roule très peu. Les pneus sont neufs. Prix : 95 euros. Je ne fais pas d'envoi : il faut venir le chercher à Liège, le samedi ou le dimanche. » Hoeveel euro kost de fiets? Schrijf alleen het getal.$v$
 where vraag = $v$Nog altijd het zoekertje. Hoeveel euro kost de fiets? Schrijf alleen het getal.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « À vendre : vélo de ville bleu, taille moyenne. Je l'ai acheté il y a deux ans et je roule très peu. Les pneus sont neufs. Prix : 95 euros. Je ne fais pas d'envoi : il faut venir le chercher à Liège, le samedi ou le dimanche. » Welke punten over de fiets staan er letterlijk in het zoekertje?$v$
 where vraag = $v$Welke punten over de fiets staan er letterlijk in het zoekertje?$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « À vendre : vélo de ville bleu, taille moyenne. Je l'ai acheté il y a deux ans et je roule très peu. Les pneus sont neufs. Prix : 95 euros. Je ne fais pas d'envoi : il faut venir le chercher à Liège, le samedi ou le dimanche. » Volgens het zoekertje stuurt de verkoper de fiets met de post op.$v$
 where vraag = $v$Volgens het zoekertje stuurt de verkoper de fiets met de post op.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « Chers parents, le lundi 12 octobre, les cours commencent à 10 h. Les professeurs ont une réunion le matin. La garderie est ouverte à partir de 8 h pour les élèves qui prennent le bus. Le repas de midi se passe comme d'habitude. » Vanaf welk uur is de opvang open? Schrijf alleen het getal.$v$
 where vraag = $v$Hetzelfde bericht van de school. Vanaf welk uur is de opvang open? Schrijf alleen het getal.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « Chers parents, le lundi 12 octobre, les cours commencent à 10 h. Les professeurs ont une réunion le matin. La garderie est ouverte à partir de 8 h pour les élèves qui prennent le bus. Le repas de midi se passe comme d'habitude. » Waarom beginnen de lessen later?$v$
 where vraag = $v$Nog het bericht van de school. Waarom beginnen de lessen later?$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « Chers parents, le lundi 12 octobre, les cours commencent à 10 h. Les professeurs ont une réunion le matin. La garderie est ouverte à partir de 8 h pour les élèves qui prennent le bus. Le repas de midi se passe comme d'habitude. » Volgens het bericht van de school verloopt het middagmaal die dag zoals altijd.$v$
 where vraag = $v$Volgens het bericht van de school verloopt het middagmaal die dag zoals altijd.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « Pour quatre personnes : coupez deux oignons et faites-les cuire cinq minutes dans un peu d'huile. Ajoutez le riz et un litre d'eau chaude. Laissez cuire vingt minutes sans couvercle. Salez à la fin, pas avant. » Hoeveel minuten moet de rijst koken? Schrijf alleen het getal.$v$
 where vraag = $v$Hetzelfde recept. Hoeveel minuten moet de rijst koken? Schrijf alleen het getal.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « Pour quatre personnes : coupez deux oignons et faites-les cuire cinq minutes dans un peu d'huile. Ajoutez le riz et un litre d'eau chaude. Laissez cuire vingt minutes sans couvercle. Salez à la fin, pas avant. » Volgens het recept zout je het gerecht pas op het einde.$v$
 where vraag = $v$Volgens het recept zout je het gerecht pas op het einde.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « Pour quatre personnes : coupez deux oignons et faites-les cuire cinq minutes dans un peu d'huile. Ajoutez le riz et un litre d'eau chaude. Laissez cuire vingt minutes sans couvercle. Salez à la fin, pas avant. » Voor hoeveel mensen is het bedoeld, en wat doe je met het deksel?$v$
 where vraag = $v$Nog het recept. Voor hoeveel mensen is het bedoeld, en wat doe je met het deksel?$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « Samedi, je suis allée à la mer avec ma cousine. Nous avons pris le train de 7 h 40 pour éviter le monde. Il faisait froid, mais le ciel était bleu. Nous avons marché deux heures sur la plage et nous avons mangé des frites. Le soir, j'avais mal aux jambes, mais j'étais contente. » Waarom namen ze de trein van 7 u 40?$v$
 where vraag = $v$Hetzelfde verslagje over de zee. Waarom namen ze de trein van 7 u 40?$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « Samedi, je suis allée à la mer avec ma cousine. Nous avons pris le train de 7 h 40 pour éviter le monde. Il faisait froid, mais le ciel était bleu. Nous avons marché deux heures sur la plage et nous avons mangé des frites. Le soir, j'avais mal aux jambes, mais j'étais contente. » In het verslagje over de zee was het warm weer met een grijze lucht.$v$
 where vraag = $v$In het verslagje over de zee was het warm weer met een grijze lucht.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 1
update vragen set vraag = $v$Lees nog eens: « Tu as entre 15 et 18 ans ? Viens essayer l'escalade gratuitement le mercredi après-midi. Pas besoin de matériel : nous prêtons tout. Inscris-toi avant le 30 septembre, le groupe est limité à douze jeunes. » Voor hoeveel jongeren is er plaats? Schrijf alleen het getal.$v$
 where vraag = $v$Dezelfde affiche. Voor hoeveel jongeren is er plaats? Schrijf alleen het getal.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Bibliothèque de Namur — lundi : fermé. Mardi et jeudi : 10 h – 18 h. Mercredi : 14 h – 19 h. Vendredi : 10 h – 16 h. Samedi : 9 h – 13 h. Fermée les jours fériés. » Op welke dag van de week is de bibliotheek gesloten? Schrijf de dag in het Nederlands.$v$
 where vraag = $v$Dezelfde openingsuren. Op welke dag van de week is de bibliotheek gesloten? Schrijf de dag in het Nederlands.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Bibliothèque de Namur — lundi : fermé. Mardi et jeudi : 10 h – 18 h. Mercredi : 14 h – 19 h. Vendredi : 10 h – 16 h. Samedi : 9 h – 13 h. Fermée les jours fériés. » Volgens die openingsuren kan je er op zaterdagnamiddag terecht.$v$
 where vraag = $v$Volgens die openingsuren kan je er op zaterdagnamiddag terecht.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Bibliothèque de Namur — lundi : fermé. Mardi et jeudi : 10 h – 18 h. Mercredi : 14 h – 19 h. Vendredi : 10 h – 16 h. Samedi : 9 h – 13 h. Fermée les jours fériés. » Op welke twee dagen gaat de bibliotheek om 10 uur open?$v$
 where vraag = $v$Nog die openingsuren. Op welke twee dagen gaat de bibliotheek om 10 uur open?$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Piscine communale — entrée adulte : 4,50 €. Jeunes de moins de 18 ans : 2,50 €. Carte de dix entrées : 20 € (jeunes) ou 38 € (adultes). Location d'une serviette : 2 €. Le bonnet de bain est obligatoire et n'est pas en location. » Hoeveel euro kost een kaart van tien beurten voor een jongere? Schrijf alleen het getal.$v$
 where vraag = $v$Dezelfde prijslijst. Hoeveel euro kost een kaart van tien beurten voor een jongere? Schrijf alleen het getal.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Piscine communale — entrée adulte : 4,50 €. Jeunes de moins de 18 ans : 2,50 €. Carte de dix entrées : 20 € (jeunes) ou 38 € (adultes). Location d'une serviette : 2 €. Le bonnet de bain est obligatoire et n'est pas en location. » Volgens de prijslijst kan je er een badmuts huren.$v$
 where vraag = $v$Volgens de prijslijst kan je er een badmuts huren.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Piscine communale — entrée adulte : 4,50 €. Jeunes de moins de 18 ans : 2,50 €. Carte de dix entrées : 20 € (jeunes) ou 38 € (adultes). Location d'une serviette : 2 €. Le bonnet de bain est obligatoire et n'est pas en location. » Twee volwassenen gaan samen één keer zwemmen en huren één handdoek. Hoeveel betalen ze?$v$
 where vraag = $v$Nog de prijslijst van het zwembad. Twee volwassenen gaan samen één keer zwemmen en huren één handdoek. Hoeveel betalen ze?$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Lou : Tu viens toujours demain ? — Sacha : Oui, mais je finis à 17 h, donc j'arrive vers 18 h 30. — Lou : Pas de souci, on mange à 19 h. Tu peux apporter un dessert ? — Sacha : D'accord. Sucré ou des fruits ? — Lou : Des fruits, il y a déjà un gâteau. » Wat moet Sacha meebrengen, en waarom net dat?$v$
 where vraag = $v$Hetzelfde gesprekje. Wat moet Sacha meebrengen, en waarom net dat?$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Lou : Tu viens toujours demain ? — Sacha : Oui, mais je finis à 17 h, donc j'arrive vers 18 h 30. — Lou : Pas de souci, on mange à 19 h. Tu peux apporter un dessert ? — Sacha : D'accord. Sucré ou des fruits ? — Lou : Des fruits, il y a déjà un gâteau. » In dat gesprekje vindt Lou het geen probleem dat Sacha later komt.$v$
 where vraag = $v$In dat gesprekje vindt Lou het geen probleem dat Sacha later komt.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Lou : Tu viens toujours demain ? — Sacha : Oui, mais je finis à 17 h, donc j'arrive vers 18 h 30. — Lou : Pas de souci, on mange à 19 h. Tu peux apporter un dessert ? — Sacha : D'accord. Sucré ou des fruits ? — Lou : Des fruits, il y a déjà un gâteau. » Hoe laat eten ze? Schrijf alleen het getal van het uur.$v$
 where vraag = $v$Nog dat gesprekje. Hoe laat eten ze? Schrijf alleen het getal van het uur.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Avant le premier lavage : lavez le vêtement seul, à 30 degrés. N'utilisez pas de sèche-linge. Repassez à l'envers, sur une température moyenne. En cas de tache, lavez tout de suite à l'eau froide. » Op hoeveel graden moet je wassen? Schrijf alleen het getal.$v$
 where vraag = $v$Hetzelfde waslabel. Op hoeveel graden moet je wassen? Schrijf alleen het getal.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Avant le premier lavage : lavez le vêtement seul, à 30 degrés. N'utilisez pas de sèche-linge. Repassez à l'envers, sur une température moyenne. En cas de tache, lavez tout de suite à l'eau froide. » Volgens dat waslabel moet je een vlek meteen met koud water uitwassen.$v$
 where vraag = $v$Volgens dat waslabel moet je een vlek meteen met koud water uitwassen.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Depuis la rentrée, les élèves de deux écoles de Charleroi laissent leur téléphone dans un casier pendant les cours. Les professeurs trouvent les classes plus calmes. Certains élèves se plaignent, mais la plupart disent qu'ils se concentrent mieux. L'école va garder la règle jusqu'en juin. » Welke punten staan er in de tekst?$v$
 where vraag = $v$Hetzelfde krantenstukje. Welke punten staan er in de tekst?$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Depuis la rentrée, les élèves de deux écoles de Charleroi laissent leur téléphone dans un casier pendant les cours. Les professeurs trouvent les classes plus calmes. Certains élèves se plaignent, mais la plupart disent qu'ils se concentrent mieux. L'école va garder la règle jusqu'en juin. » Volgens dat krantenstukje is elke leerling tevreden met de regel.$v$
 where vraag = $v$Volgens dat krantenstukje is elke leerling tevreden met de regel.$v$;

-- boost-dubbele-finaliteit/frans.json | Een Franse tekst begrijpen — deel 2
update vragen set vraag = $v$Lees nog eens: « Madame, Je vous écris au sujet de votre annonce pour un job d'été. Je suis élève en quatrième année et je cherche du travail en juillet. J'ai déjà aidé dans le magasin de mes grands-parents, donc je connais la caisse. Je suis libre du 1er au 31 juillet, sauf le week-end du 14. Pourriez-vous me dire quand je peux venir me présenter ? » Wanneer is de leerling niet vrij?$v$
 where vraag = $v$Dezelfde mail. Wanneer is de leerling niet vrij?$v$;

-- boost-dubbele-finaliteit/frans.json | Tekstsoorten, tekstverbanden en leesstrategieën — deel 2
update vragen set vraag = $v$Lees nog eens: « Le marché est moins cher que le supermarché, par contre il n'ouvre que le mercredi. Comme je travaille ce jour-là, j'y vais rarement. Donc j'achète mes légumes au magasin du coin, même si c'est dommage. » Welk woord geeft daar een gevolg aan?$v$
 where vraag = $v$Hetzelfde tekstje over de markt. Welk woord geeft daar een gevolg aan?$v$;

-- boost-dubbele-finaliteit/frans.json | Tekstsoorten, tekstverbanden en leesstrategieën — deel 2
update vragen set vraag = $v$Lees nog eens: « Le marché est moins cher que le supermarché, par contre il n'ouvre que le mercredi. Comme je travaille ce jour-là, j'y vais rarement. Donc j'achète mes légumes au magasin du coin, même si c'est dommage. » In dat tekstje over de markt geeft comme je travaille ce jour-là een reden.$v$
 where vraag = $v$In dat tekstje over de markt geeft comme je travaille ce jour-là een reden.$v$;

-- boost-dubbele-finaliteit/frans.json | Tekstsoorten, tekstverbanden en leesstrategieën — deel 2
update vragen set vraag = $v$Lees nog eens: « L'atelier est complet pour le mois de mars. Cependant, nous ouvrons un deuxième groupe en avril. Si vous êtes intéressé, répondez avant le 1er mars, car les places partent vite. » Welk woord geeft de reden waarom je snel moet antwoorden?$v$
 where vraag = $v$Hetzelfde tekstje over de workshop. Welk woord geeft de reden waarom je snel moet antwoorden?$v$;

-- boost-dubbele-finaliteit/frans.json | Tekstsoorten, tekstverbanden en leesstrategieën — deel 2
update vragen set vraag = $v$Lees nog eens: « Nos voisins ont un grand jardin. Ils y cultivent des tomates et des haricots. L'été dernier, ils nous en ont donné un plein panier. Nous les avons remerciés avec une tarte. » Waarnaar verwijst y in Ils y cultivent des tomates?$v$
 where vraag = $v$Hetzelfde tekstje over de buren. Waarnaar verwijst y in Ils y cultivent des tomates?$v$;

-- boost-dubbele-finaliteit/frans.json | Tekstsoorten, tekstverbanden en leesstrategieën — deel 2
update vragen set vraag = $v$Lees nog eens: « Nos voisins ont un grand jardin. Ils y cultivent des tomates et des haricots. L'été dernier, ils nous en ont donné un plein panier. Nous les avons remerciés avec une tarte. » Naar wie verwijst les in Nous les avons remerciés?$v$
 where vraag = $v$Nog dat tekstje over de buren. Naar wie verwijst les in Nous les avons remerciés?$v$;

-- boost-dubbele-finaliteit/frans.json | Tekstsoorten, tekstverbanden en leesstrategieën — deel 2
update vragen set vraag = $v$Lees nog eens: « Nos voisins ont un grand jardin. Ils y cultivent des tomates et des haricots. L'été dernier, ils nous en ont donné un plein panier. Nous les avons remerciés avec une tarte. » In datzelfde tekstje vervangt en in ils nous en ont donné de buren.$v$
 where vraag = $v$In datzelfde tekstje vervangt en in ils nous en ont donné de buren.$v$;

-- boost-dubbele-finaliteit/frans.json | De Franstalige wereld: omgangsvormen en gewoontes — deel 1
update vragen set vraag = $v$Lees nog eens: « Au travail, j'appelle mes collègues par leur prénom et on se dit tu. Mais quand un client entre, je passe au vous, même s'il a mon âge. Et je recommence à dire vous à un collègue que je ne connais pas encore. » Volgens dat tekstje over het werk hangt de keuze tussen tu en vous af van de leeftijd van de andere persoon.$v$
 where vraag = $v$Volgens dat tekstje over het werk hangt de keuze tussen tu en vous af van de leeftijd van de andere persoon.$v$;

-- boost-dubbele-finaliteit/frans.json | De Franstalige wereld: omgangsvormen en gewoontes — deel 2
update vragen set vraag = $v$Lees nog eens: « En Belgique, trois langues sont officielles : le néerlandais, le français et l'allemand. Le français est la langue de la Wallonie et, avec le néerlandais, de Bruxelles. Un Belge francophone dit septante et nonante, là où un Français dit soixante-dix et quatre-vingt-dix. » Welk Frans woord gebruikt een Belg voor negentig, waar een Fransman quatre-vingt-dix zegt? Schrijf het woord.$v$
 where vraag = $v$Hetzelfde tekstje over België. Welk Frans woord gebruikt een Belg voor negentig, waar een Fransman quatre-vingt-dix zegt? Schrijf het woord.$v$;

-- boost-dubbele-finaliteit/frans.json | De Franstalige wereld: omgangsvormen en gewoontes — deel 2
update vragen set vraag = $v$Lees nog eens: « En Belgique, trois langues sont officielles : le néerlandais, le français et l'allemand. Le français est la langue de la Wallonie et, avec le néerlandais, de Bruxelles. Un Belge francophone dit septante et nonante, là où un Français dit soixante-dix et quatre-vingt-dix. » Volgens dat tekstje spreken Belgen en Fransen een verschillende taal.$v$
 where vraag = $v$Volgens dat tekstje spreken Belgen en Fransen een verschillende taal.$v$;

-- boost-dubbele-finaliteit/frans.json | De Franstalige wereld: omgangsvormen en gewoontes — deel 2
update vragen set vraag = $v$Lees nog eens: « Le français n'est pas parlé qu'en France. On le parle aussi en Belgique, en Suisse, au Luxembourg, au Québec et dans de nombreux pays d'Afrique. Les mots et l'accent ne sont pas partout les mêmes, mais on se comprend. » Welke plaatsen noemt het waar Frans gesproken wordt?$v$
 where vraag = $v$Hetzelfde tekstje. Welke plaatsen noemt het waar Frans gesproken wordt?$v$;

-- boost-dubbele-finaliteit/frans.json | De Franstalige wereld: omgangsvormen en gewoontes — deel 2
update vragen set vraag = $v$Lees nog eens: « Le français n'est pas parlé qu'en France. On le parle aussi en Belgique, en Suisse, au Luxembourg, au Québec et dans de nombreux pays d'Afrique. Les mots et l'accent ne sont pas partout les mêmes, mais on se comprend. » Volgens dat tekstje klinkt het Frans overal in de wereld precies hetzelfde.$v$
 where vraag = $v$Volgens dat tekstje klinkt het Frans overal in de wereld precies hetzelfde.$v$;

-- boost-dubbele-finaliteit/frans.json | De Franstalige wereld: omgangsvormen en gewoontes — deel 2
update vragen set vraag = $v$Lees nog eens: « Le 21 juillet, la Belgique fête sa fête nationale : il y a un défilé à Bruxelles et les écoles sont fermées, mais c'est les vacances. En France, la fête nationale est le 14 juillet, avec des feux d'artifice le soir du 13 ou du 14. » Op welke dag van juli viert België zijn nationale feestdag? Schrijf alleen het getal.$v$
 where vraag = $v$Hetzelfde tekstje. Op welke dag van juli viert België zijn nationale feestdag? Schrijf alleen het getal.$v$;

-- boost-dubbele-finaliteit/frans.json | De Franstalige wereld: omgangsvormen en gewoontes — deel 2
update vragen set vraag = $v$Lees nog eens: « Le 21 juillet, la Belgique fête sa fête nationale : il y a un défilé à Bruxelles et les écoles sont fermées, mais c'est les vacances. En France, la fête nationale est le 14 juillet, avec des feux d'artifice le soir du 13 ou du 14. » Volgens dat tekstje vallen de twee nationale feestdagen in dezelfde maand.$v$
 where vraag = $v$Volgens dat tekstje vallen de twee nationale feestdagen in dezelfde maand.$v$;

-- boost-dubbele-finaliteit/frans.json | De Franstalige wereld: omgangsvormen en gewoontes — deel 2
update vragen set vraag = $v$Lees nog eens: « Dans beaucoup de villes françaises, les magasins ferment entre midi et deux heures, surtout dans les petites rues. Le dimanche, seule la boulangerie est ouverte, et souvent le matin seulement. » Volgens datzelfde tekstje blijven kleine Franse winkels over de middag vaak twee uur toe.$v$
 where vraag = $v$Volgens datzelfde tekstje blijven kleine Franse winkels over de middag vaak twee uur toe.$v$;

-- boost-dubbele-finaliteit/frans.json | De Franstalige wereld: omgangsvormen en gewoontes — deel 2
update vragen set vraag = $v$Lees nog eens: « Chez nous, le repas principal est le soir, vers 19 h 30 ou 20 h. On commence souvent par une entrée, puis le plat, et le fromage vient avant le dessert. Le pain reste sur la table pendant tout le repas, à côté de l'assiette. » Volgens datzelfde tekstje over de maaltijd is het middagmaal de hoofdmaaltijd.$v$
 where vraag = $v$Volgens datzelfde tekstje over de maaltijd is het middagmaal de hoofdmaaltijd.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: mens, familie, gevoelens en gezondheid — deel 1
update vragen set vraag = $v$Lees nog eens: « Nom : Dubois. Prénom : Camille. Date de naissance : 14 mars 2010. Lieu de naissance : Namur. Nationalité : belge. Adresse : rue des Écoles 12, 5000 Namur. Numéro de téléphone : 0470 12 34 56. Adresse mail : camille.dubois@exemple.be » In welke maand is Camille geboren? Schrijf de maand in het Nederlands.$v$
 where vraag = $v$Hetzelfde formulier. In welke maand is Camille geboren? Schrijf de maand in het Nederlands.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: mens, familie, gevoelens en gezondheid — deel 1
update vragen set vraag = $v$Lees nog eens: « Nom : Dubois. Prénom : Camille. Date de naissance : 14 mars 2010. Lieu de naissance : Namur. Nationalité : belge. Adresse : rue des Écoles 12, 5000 Namur. Numéro de téléphone : 0470 12 34 56. Adresse mail : camille.dubois@exemple.be » Op dat formulier staat bij lieu de naissance de geboorteplaats.$v$
 where vraag = $v$Op dat formulier staat bij lieu de naissance de geboorteplaats.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: mens, familie, gevoelens en gezondheid — deel 1
update vragen set vraag = $v$Lees nog eens: « Hier, j'étais vraiment fatiguée, et un peu triste aussi. Ce matin, ça va beaucoup mieux : j'ai reçu une bonne nouvelle et je suis contente. Mon frère, lui, est en colère parce que son équipe a perdu. » Waarom is haar broer boos?$v$
 where vraag = $v$Hetzelfde tekstje. Waarom is haar broer boos?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: mens, familie, gevoelens en gezondheid — deel 2
update vragen set vraag = $v$Lees nog eens: « — Bonjour, qu'est-ce qui ne va pas ? — J'ai mal au ventre depuis deux jours, docteur. — Vous avez de la fièvre ? — Non, mais je dors mal. — Je vous donne une ordonnance. Prenez un comprimé matin et soir, pendant cinq jours. » Wat moet de patiënt doen?$v$
 where vraag = $v$Hetzelfde gesprekje. Wat moet de patiënt doen?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: mens, familie, gevoelens en gezondheid — deel 2
update vragen set vraag = $v$Lees nog eens: « À la pharmacie, vous pouvez acheter du paracétamol sans ordonnance. Pour un antibiotique, il faut une ordonnance du médecin. Demandez conseil au pharmacien : il vous dira aussi combien de temps vous pouvez prendre un médicament. » Welke twee dingen kan de apotheker voor je doen?$v$
 where vraag = $v$Hetzelfde tekstje. Welke twee dingen kan de apotheker voor je doen?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: mens, familie, gevoelens en gezondheid — deel 2
update vragen set vraag = $v$Lees nog eens: « À la pharmacie, vous pouvez acheter du paracétamol sans ordonnance. Pour un antibiotique, il faut une ordonnance du médecin. Demandez conseil au pharmacien : il vous dira aussi combien de temps vous pouvez prendre un médicament. » Volgens dat tekstje kan je paracetamol alleen met een voorschrift kopen.$v$
 where vraag = $v$Volgens dat tekstje kan je paracetamol alleen met een voorschrift kopen.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: eten, kleding, wonen en winkelen — deel 2
update vragen set vraag = $v$Lees nog eens: « L'appartement a deux chambres, une cuisine équipée et une petite salle de bains. Le salon donne sur un balcon. Il y a un lave-linge dans la cave. Le loyer est de 650 euros par mois, charges comprises. » Hoeveel euro is de huur per maand? Schrijf alleen het getal.$v$
 where vraag = $v$Hetzelfde zoekertje. Hoeveel euro is de huur per maand? Schrijf alleen het getal.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: eten, kleding, wonen en winkelen — deel 2
update vragen set vraag = $v$Lees nog eens: « L'appartement a deux chambres, une cuisine équipée et une petite salle de bains. Le salon donne sur un balcon. Il y a un lave-linge dans la cave. Le loyer est de 650 euros par mois, charges comprises. » Waar staat de wasmachine?$v$
 where vraag = $v$Nog dat zoekertje. Waar staat de wasmachine?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: eten, kleding, wonen en winkelen — deel 2
update vragen set vraag = $v$Lees nog eens: « L'appartement a deux chambres, une cuisine équipée et une petite salle de bains. Le salon donne sur un balcon. Il y a un lave-linge dans la cave. Le loyer est de 650 euros par mois, charges comprises. » Volgens dat zoekertje zijn de kosten bij de huurprijs inbegrepen.$v$
 where vraag = $v$Volgens dat zoekertje zijn de kosten bij de huurprijs inbegrepen.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: school, werk en de professionele wereld — deel 1
update vragen set vraag = $v$Lees nog eens: « Je suis en quatrième année. Mes cours préférés sont le français et les sciences. Les maths, c'est plus difficile pour moi, mais j'ai un bon professeur. Nous avons cours de huit heures vingt à quatre heures, avec une heure de midi. Le mercredi, on finit à midi. » Hoe laat is de school op woensdag gedaan?$v$
 where vraag = $v$Hetzelfde tekstje. Hoe laat is de school op woensdag gedaan?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: school, werk en de professionele wereld — deel 1
update vragen set vraag = $v$Lees nog eens: « Bulletin du premier trimestre — Français : 14/20. Mathématiques : 11/20. Sciences : 16/20. Éducation physique : 15/20. Remarque du titulaire : élève attentif, mais doit rendre ses devoirs à temps. » Wat moet deze leerling volgens de titularis beter doen?$v$
 where vraag = $v$Hetzelfde rapport. Wat moet deze leerling volgens de titularis beter doen?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: school, werk en de professionele wereld — deel 1
update vragen set vraag = $v$Lees nog eens: « Dans ma famille, tout le monde travaille avec les mains. Mon père est électricien, ma mère est infirmière et mon oncle est boulanger. Moi, je voudrais devenir éducateur. Ma sœur, elle, veut travailler dans un bureau. » Wat wil de schrijver worden?$v$
 where vraag = $v$Hetzelfde tekstje. Wat wil de schrijver worden?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: school, werk en de professionele wereld — deel 2
update vragen set vraag = $v$Lees nog eens: « Mon stage s'est bien passé. Le premier jour, j'avais peur de mal faire, mais l'équipe m'a aidé. J'ai appris à répondre au téléphone et à classer des documents. Ce que j'ai trouvé difficile, c'est de rester assis toute la journée. Je recommencerais quand même. » Wat heeft de leerling geleerd?$v$
 where vraag = $v$Hetzelfde verslagje. Wat heeft de leerling geleerd?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: school, werk en de professionele wereld — deel 2
update vragen set vraag = $v$Lees nog eens: « Mon stage s'est bien passé. Le premier jour, j'avais peur de mal faire, mais l'équipe m'a aidé. J'ai appris à répondre au téléphone et à classer des documents. Ce que j'ai trouvé difficile, c'est de rester assis toute la journée. Je recommencerais quand même. » Volgens dat verslagje zou de leerling de stage opnieuw doen.$v$
 where vraag = $v$Volgens dat verslagje zou de leerling de stage opnieuw doen.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: school, werk en de professionele wereld — deel 2
update vragen set vraag = $v$Lees nog eens: « Magasin de sport cherche étudiant pour les samedis. Tâches : accueillir les clients, ranger les rayons, aider à la caisse. Expérience non exigée. Envoyez votre CV par mail avant le 15 du mois. » Wat betekent expérience non exigée?$v$
 where vraag = $v$Hetzelfde zoekertje. Wat betekent expérience non exigée?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: school, werk en de professionele wereld — deel 2
update vragen set vraag = $v$Lees nog eens: « Magasin de sport cherche étudiant pour les samedis. Tâches : accueillir les clients, ranger les rayons, aider à la caisse. Expérience non exigée. Envoyez votre CV par mail avant le 15 du mois. » Op welke dag van de week zoekt de winkel iemand? Schrijf de dag in het Nederlands.$v$
 where vraag = $v$Nog dat zoekertje. Op welke dag van de week zoekt de winkel iemand? Schrijf de dag in het Nederlands.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: school, werk en de professionele wereld — deel 2
update vragen set vraag = $v$Lees nog eens: « Je joue au basket depuis cinq ans, deux fois par semaine. Le samedi, il y a souvent un match. Quand je ne joue pas, je regarde des séries ou je lis. Ma sœur, elle, fait de la danse et joue du piano. » Wat doet de zus?$v$
 where vraag = $v$Hetzelfde tekstje. Wat doet de zus?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: tijd, weer, reizen en vervoer — deel 1
update vragen set vraag = $v$Lees nog eens: « Lundi : cours jusqu'à quatre heures. Mardi : dentiste à dix-sept heures trente. Mercredi après-midi : libre. Jeudi : entraînement de basket. Vendredi : anniversaire de Lila. Samedi matin : courses. Dimanche : rien, enfin. » Hoe laat is de tandarts?$v$
 where vraag = $v$Dezelfde agenda. Hoe laat is de tandarts?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: tijd, weer, reizen en vervoer — deel 1
update vragen set vraag = $v$Lees nog eens: « Lundi : cours jusqu'à quatre heures. Mardi : dentiste à dix-sept heures trente. Mercredi après-midi : libre. Jeudi : entraînement de basket. Vendredi : anniversaire de Lila. Samedi matin : courses. Dimanche : rien, enfin. » Op welke dag is er basketbaltraining? Schrijf de dag in het Nederlands.$v$
 where vraag = $v$Nog die agenda. Op welke dag is er basketbaltraining? Schrijf de dag in het Nederlands.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: tijd, weer, reizen en vervoer — deel 1
update vragen set vraag = $v$Lees nog eens: « En Belgique, le printemps commence en mars et l'été en juin. Les grandes vacances durent de juillet à fin août. L'automne apporte la pluie et les feuilles mortes, et l'hiver les jours courts. Noël tombe le 25 décembre, le Nouvel An le 1er janvier. » Wanneer valt Nieuwjaar?$v$
 where vraag = $v$Nog dat tekstje. Wanneer valt Nieuwjaar?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: tijd, weer, reizen en vervoer — deel 1
update vragen set vraag = $v$Lees nog eens: « En Belgique, le printemps commence en mars et l'été en juin. Les grandes vacances durent de juillet à fin août. L'automne apporte la pluie et les feuilles mortes, et l'hiver les jours courts. Noël tombe le 25 décembre, le Nouvel An le 1er janvier. » Volgens dat tekstje lopen de grote vakantie van juli tot eind augustus.$v$
 where vraag = $v$Volgens dat tekstje lopen de grote vakantie van juli tot eind augustus.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: tijd, weer, reizen en vervoer — deel 2
update vragen set vraag = $v$Lees nog eens: « Demain, le temps restera gris dans tout le pays. Il pleuvra le matin en Wallonie, avec un vent assez fort venant de l'ouest. Les températures ne dépasseront pas douze degrés. En fin de journée, quelques éclaircies à la côte. » Hoeveel graden wordt het maximaal? Schrijf alleen het getal.$v$
 where vraag = $v$Hetzelfde weerbericht. Hoeveel graden wordt het maximaal? Schrijf alleen het getal.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: tijd, weer, reizen en vervoer — deel 2
update vragen set vraag = $v$Lees nog eens: « Demain, le temps restera gris dans tout le pays. Il pleuvra le matin en Wallonie, avec un vent assez fort venant de l'ouest. Les températures ne dépasseront pas douze degrés. En fin de journée, quelques éclaircies à la côte. » Uit welke richting komt de wind?$v$
 where vraag = $v$Nog dat weerbericht. Uit welke richting komt de wind?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: tijd, weer, reizen en vervoer — deel 2
update vragen set vraag = $v$Lees nog eens: « Demain, le temps restera gris dans tout le pays. Il pleuvra le matin en Wallonie, avec un vent assez fort venant de l'ouest. Les températures ne dépasseront pas douze degrés. En fin de journée, quelques éclaircies à la côte. » Volgens dat weerbericht komen er op het einde van de dag opklaringen aan de kust.$v$
 where vraag = $v$Volgens dat weerbericht komen er op het einde van de dag opklaringen aan de kust.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: tijd, weer, reizen en vervoer — deel 2
update vragen set vraag = $v$Lees nog eens: « Le train de 14 h 05 vers Namur a un retard de vingt minutes. Les voyageurs pour Charleroi doivent changer à Ottignies. Le train suivant part à 14 h 35, voie 3. » Wat moeten de reizigers naar Charleroi doen?$v$
 where vraag = $v$Hetzelfde bericht. Wat moeten de reizigers naar Charleroi doen?$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: tijd, weer, reizen en vervoer — deel 2
update vragen set vraag = $v$Lees nog eens: « L'été dernier, nous sommes partis dix jours en Espagne. Nous avons pris l'avion jusqu'à Barcelone, puis le train jusqu'à la côte. L'hôtel était simple mais propre, et la mer était à deux cents mètres. Je voudrais y retourner. » Hoeveel dagen zijn ze weggeweest? Schrijf alleen het getal.$v$
 where vraag = $v$Hetzelfde verslagje. Hoeveel dagen zijn ze weggeweest? Schrijf alleen het getal.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: tijd, weer, reizen en vervoer — deel 2
update vragen set vraag = $v$Lees nog eens: « L'été dernier, nous sommes partis dix jours en Espagne. Nous avons pris l'avion jusqu'à Barcelone, puis le train jusqu'à la côte. L'hôtel était simple mais propre, et la mer était à deux cents mètres. Je voudrais y retourner. » Volgens dat verslagje lag het hotel ver van de zee.$v$
 where vraag = $v$Volgens dat verslagje lag het hotel ver van de zee.$v$;

-- boost-dubbele-finaliteit/frans.json | Woordvelden: tijd, weer, reizen en vervoer — deel 2
update vragen set vraag = $v$Lees nog eens: « Dans ma classe, il y a des élèves de partout. Yacine est marocain, Lena est allemande, Mateo vient d'Italie et Noor est née en Belgique. On parle français entre nous, mais chacun connaît encore une autre langue. » Uit welk land komt Mateo? Schrijf het land in het Nederlands.$v$
 where vraag = $v$Hetzelfde tekstje. Uit welk land komt Mateo? Schrijf het land in het Nederlands.$v$;

-- Hoeveel vragen dragen hun tekst nu zelf?
select count(*) as aangepast
  from vragen
 where vraag like 'Lees nog eens%'
    or vraag like 'Je ziet een Engelse cartoon%';
