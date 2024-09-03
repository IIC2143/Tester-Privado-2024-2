from src.models import Game, Review, Player


GAMES_A = [
    Game(name='Elden_Ring', calification=4.9, description='Juego de rol y acción con un vasto mundo abierto y un diseño desafiante.'),
    Game(name='Ghost_of_Tsushima', calification=4.8, description='Juego de acción y aventura ambientado en el Japón feudal.'),
    Game(name='Hades', calification=4.7, description='Juego de acción tipo rogue-like con una narrativa envolvente.'),
    Game(name='Animal_Crossing:_New_Horizons', calification=4.6, description='Simulación de vida en una isla desierta con actividades relajantes.'),
    Game(name='Persona_5_Royal', calification=4.9, description='Juego de rol japonés con una historia envolvente y personajes carismáticos.'),
    Game(name='Final_Fantasy_VII_Remake', calification=4.8, description='Reimaginación de un clásico juego de rol con gráficos modernizados.'),
    Game(name='Among_Us', calification=4.3, description='Juego de deducción social multijugador con traición y trabajo en equipo.')
]

REVIEWS_A = [
    Review(title='Epopeya_fantasmal_en_Elden_Ring', description='Elden Ring es una experiencia de fantasía oscura con un diseño de mundo interconectado y un desafío implacable.', calification=4.9),
    Review(title='Belleza_y_honor_en_Ghost_of_Tsushima', description='Ghost of Tsushima captura la esencia del Japón feudal con combates fluidos y un hermoso paisaje.', calification=4.8),
    Review(title='Intensidad_y_mitología_en_Hades', description='Hades ofrece combates rápidos y estratégicos con una historia mitológica fascinante.', calification=4.7),
    Review(title='Vida_relajada_en_Animal_Crossing:_New_Horizons', description='Animal Crossing: New Horizons es el juego perfecto para relajarse y disfrutar de la vida en una isla personalizada.', calification=4.6),
    Review(title='Obra_maestra_japonesa_en_Persona_5_Royal', description='Persona 5 Royal es un juego de rol profundo con una narrativa intrigante y personajes inolvidables.', calification=4.9),
    Review(title='Nostalgia_modernizada_en_Final_Fantasy_VII_Remake', description='Final Fantasy VII Remake lleva el clásico a nuevas alturas con gráficos impresionantes y un sistema de combate renovado.', calification=4.8),
    Review(title='Tensión_y_traición_en_Among_Us', description='Among Us es una experiencia multijugador llena de tensión, traición y trabajo en equipo.', calification=4.3)
]

PLAYERS_A = [
    Player(name='Doublelift', preference='MOBA', phone='789-123-4560'),
    Player(name='Shroud', preference='Shooter', phone='890-234-5671'),
    Player(name='Scarlett', preference='Strategy', phone='901-345-6782'),
    Player(name='Hungrybox', preference='Fighting', phone='012-456-7893'),
    Player(name='C9_Mang0', preference='Fighting', phone='123-567-8904'),
    Player(name='Thorin', preference='Strategy', phone='234-678-9015'),
    Player(name='iDom', preference='Fighting', phone='345-789-0126')
]

GAMES_B = [
    Game(name='God_of_War', calification=4.9, description='Juego de acción y aventura mitológica.'),
    Game(name='The_Last_of_Us_Part_II', calification=4.8, description='Juego de acción y aventura con una narrativa emocional.'),
    Game(name='Grand_Theft_Auto_V', calification=4.8, description='Juego de acción y aventura en un mundo abierto.'),
    Game(name='Overwatch', calification=4.5, description='Juego de disparos en primera persona en equipo.'),
    Game(name='Dark_Souls_III', calification=4.6, description='Juego de rol de acción con alta dificultad.'),
    Game(name='Horizon_Zero_Dawn', calification=4.7, description='Juego de rol y acción en un futuro post-apocalíptico.'),
    Game(name='Doom_Eternal', calification=4.7, description='Juego de disparos en primera persona con acción intensa.')
]

REVIEWS_B = [
    Review(title='Épico_viaje_mitológico_en_God_of_War', description='God of War redefine la serie con una emocionante aventura mitológica.', calification=4.9),
    Review(title='Emocional_y_brutal_en_The_Last_of_Us_Part_II', description='The Last of Us Part II es una montaña rusa emocional con una jugabilidad excelente.', calification=4.8),
    Review(title='Libertad_y_crimen_en_GTA_V', description='Grand Theft Auto V ofrece un vasto mundo abierto lleno de actividades y una historia intrigante.', calification=4.8),
    Review(title='Acción_en_equipo_en_Overwatch', description='Overwatch es un juego de disparos en equipo con personajes únicos y una jugabilidad adictiva.', calification=4.5),
    Review(title='Desafío_incesante_en_Dark_Souls_III', description='Dark Souls III ofrece una experiencia desafiante y gratificante en un mundo oscuro y peligroso.', calification=4.6),
    Review(title='Futuro_apocalíptico_en_Horizon_Zero_Dawn', description='Horizon Zero Dawn combina una narrativa fascinante con una jugabilidad impresionante.', calification=4.7),
    Review(title='Acción_intensa_en_Doom_Eternal', description='Doom Eternal es pura adrenalina con combates intensos y un diseño de niveles excepcional.', calification=4.7)
]

PLAYERS_B = [
    Player(name='Cristian_Ruz', preference='Shooter', phone='123-456-7890'),
    Player(name='Moises_Retamal', preference='RPG', phone='234-567-8901'),
    Player(name='Caps', preference='MOBA', phone='765-432-1098'),
    Player(name='Xyp9x', preference='Shooter', phone='654-321-0987'),
    Player(name='Perkz', preference='MOBA', phone='543-210-9876'),
    Player(name='Mongraal', preference='Battle Royale', phone='432-109-8765'),
    Player(name='kennyS', preference='Shooter', phone='321-098-7654')
]

GAMES_C = [
    Game(name='Assassins_Creed_Valhalla', calification=4.5, description='Juego de rol y acción ambientado en la era vikinga.'),
    Game(name='Call_of_Duty:_Modern_Warfare', calification=4.6, description='Juego de disparos en primera persona con una campaña intensa.'),
    Game(name='Resident_Evil_2_Remake', calification=4.7, description='Juego de survival horror con gráficos modernizados.'),
    Game(name='Sekiro:_Shadows_Die_Twice', calification=4.8, description='Juego de acción y aventura con combates desafiantes.'),
    Game(name='Apex_Legends', calification=4.4, description='Juego de batalla real con personajes únicos y habilidades.'),
    Game(name='Control', calification=4.3, description='Juego de acción y aventura con elementos sobrenaturales.'),
    Game(name='Stardew_Valley', calification=4.9, description='Juego de simulación de granja con muchas actividades y relaciones.')
]

REVIEWS_C = [
    Review(title='Épica_aventura_vikinga_en_Valhalla', description='Assassin\'s Creed Valhalla ofrece una experiencia vikinga envolvente con combates épicos.', calification=4.5),
    Review(title='Intensidad_y_realismo_en_Modern_Warfare', description='Call of Duty: Modern Warfare redefine el género con su realismo y acción intensa.', calification=4.6),
    Review(title='Horror_reimaginado_en_Resident_Evil_2', description='Resident Evil 2 Remake es una reinvención magistral del clásico de survival horror.', calification=4.7),
    Review(title='Desafío_y_precisión_en_Sekiro', description='Sekiro: Shadows Die Twice es una prueba de habilidad con combates precisos y exigentes.', calification=4.8),
    Review(title='Batalla_real_con_estilo_en_Apex_Legends', description='Apex Legends ofrece una experiencia de batalla real rápida y llena de acción con personajes diversos.', calification=4.4),
    Review(title='Misterio_sobrenatural_en_Control', description='Control combina una narrativa intrigante con poderes sobrenaturales en un entorno único.', calification=4.3),
    Review(title='Vida_de_granja_en_Stardew_Valley', description='Stardew Valley es una experiencia de simulación de granja encantadora y adictiva.', calification=4.9)
]

PLAYERS_C = [
    Player(name='ZywOo', preference='Shooter', phone='987-654-3210'),
    Player(name='S1mple', preference='Shooter', phone='876-543-2109'),
    Player(name='Tenz', preference='Shooter', phone='765-432-1098'),
    Player(name='Ninja', preference='Battle Royale', phone='654-321-0987'),
    Player(name='DrDisrespect', preference='Shooter', phone='543-210-9876'),
    Player(name='Shroud', preference='Shooter', phone='432-109-8765'),
    Player(name='Faker', preference='MOBA', phone='321-098-7654')
]

WRONG_GAMES = [
    Game(name=' ', calification=0, description='Un juego de acción y aventura en un mundo abierto.'),
    Game(name='Red_Dead_Redemption_2', calification=-1, description='Juego de acción y aventura con un entorno de mundo abierto en el Salvaje Oeste.'),
    Game(name='The_Witcher_3:_Wild_Hunt', calification=4.9, description=' '),
    Game(name='Minecraft', calification=4.7, description='Juego de construcción, exploración y supervivencia en un mundo de bloques.'),
    Game(name='Super_Mario_Odyssey', calification=4.8, description=' ')
]

WRONG_REVIEWS = [
    Review(title=' ', description='Breath of the Wild ofrece una libertad sin precedentes y un mundo abierto lleno de sorpresas y desafíos.', calification=4.9),
    Review(title='Una_obra_maestra_del_Salvaje_Oeste', description=' ', calification=4.8),
    Review(title='El_pináculo_del_RPG_moderno', description='The Witcher 3: Wild Hunt combina una narrativa profunda con un vasto mundo abierto lleno de aventuras.', calification=0.0),
    Review(title=' ', description='Minecraft permite a los jugadores desatar su creatividad en un mundo infinito de bloques.', calification=4.7),
    Review(title='Una_aventura_global_con_Mario', description=' ', calification=4.8)
]

WRONG_PLAYERS = [
    Player(name=' ', preference='Shooter', phone='123-456-7890'),
    Player(name='s1mple', preference=' ', phone='234-567-8901'),
    Player(name='N0tail', preference='MOBA', phone=' '),
    Player(name=' ', preference=' ', phone='456-789-0123'),
    Player(name='Coldzera', preference='Shooter', phone='567-890-1234')
]
