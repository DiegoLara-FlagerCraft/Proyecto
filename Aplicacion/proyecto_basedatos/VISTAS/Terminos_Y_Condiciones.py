from tkinter import S


def Crear_Terminos_Y_Condiciones():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont

    Termininos_Y_Condiciones = tk.Tk()
    Termininos_Y_Condiciones.config(width=1360, height=768, bg= '#7EADB0')
    Termininos_Y_Condiciones.title("TERMINOS Y CONDICIONES")
    BienvenidaLabel_Usu = tk.Label(Termininos_Y_Condiciones, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Usu = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Usu = tk.Label(Termininos_Y_Condiciones,text="TERMINOS Y CONDICIONES",font=FontLabel_Usu,background='#7EADB0',justify=CENTER).place(x=450, y=50)

    
    Terminos = tk.Label(Termininos_Y_Condiciones, text= """TÉRMINOS Y CONDICIONES DE USO

GENERALIDADES

Innovate Whit Proyects gestiona este aplicativo. En todo el sitio, los términos "nosotros", "nos" y "nuestro" se refieren en lo sucesivo a Innovate Whit Proyects. Innovate Whit Proyects ofrece esta aplicativo, incluida toda la información, las herramientas y los servicios que se ponen en este sitio a disposición suya, el usuario, siempre y cuando acepte la totalidad de los términos, condiciones, políticas y avisos contemplados aquí. Al visitar nuestro sitio y/o comprarnos algo, usted interactúa con nuestro "Servicio" y reconoce como vinculantes los siguientes términos y condiciones (denominados en lo sucesivo "Términos del servicio", "Términos"), incluidos aquellos términos y condiciones adicionales y las políticas que se mencionan aquí y/o disponibles por medio de hipervínculo. Estos Términos del servicio se aplican a todos los usuarios del sitio, incluyendo de manera enunciativa mas no limitativa los usuarios que son navegadores, proveedores, clientes, comerciantes y/o que aporten contenido. Lea estos Términos del servicio detenidamente antes de acceder o utilizar nuestra aplicativo o aplicación móvil. Al acceder o utilizar cualquier parte de la aplicación web o móvil, a partir de aquí aplicación, usted acepta estos Términos del servicio. Si no acepta la totalidad de los términos y condiciones de este acuerdo, no podrá acceder al aplicativo ni utilizar ningún servicio. Si estos Términos del servicio se considerasen una oferta, la aceptación se limita expresamente a los presentes Términos del servicio. Las nuevas funciones o herramientas que se agreguen también estarán sujetas a los Términos del servicio. Puede revisar la versión más reciente de los Términos del servicio en cualquier momento en esta página. Nos reservamos el derecho de actualizar, cambiar o reemplazar cualquier parte de los presentes Términos del servicio mediante la publicación de actualizaciones o cambios en nuestra aplicativo. Es su responsabilidad revisar esta página periódicamente para ver los cambios. Su uso de la aplicativo o el acceso a ella de forma continuada después de la publicación de cualquier cambio constituye la aceptación de dichos cambios.

SECCIÓN 1: TERMINOS DE LA APLICACIÓN
 
No puede utilizar nuestros productos para ningún fin ilegal o no autorizado ni puede, al hacer uso del Servicio, infringir las leyes de su jurisdicción (incluyendo de manera enunciativa más no limitativa, las leyes de derechos de autor). Si es menor de edad puede hacer uso de nuestros servicios, bajo su propia responsabilidad ya que este no esta destinado a uso exclusivo de mayores de edad porque tiene fines también educativos. La información que ingrese o provea a Innovate Whit Proyects será pública para los usuarios que hacen uso de nuestros servicios. No transmitirá ningún gusano o virus informáticos ni ningún código de naturaleza destructiva. El incumplimiento o violación de cualquiera de los Términos dará como resultado la rescisión inmediata de sus Servicios.

SECCIÓN 2: CONDICIONES GENERALES

Nos reservamos el derecho de rechazar el servicio a cualquier persona, por cualquier motivo, en cualquier momento. Los encabezados utilizados en este acuerdo se incluyen solo para facilitar la lectura y no limitarán ni afectarán los presentes Términos.

SECCIÓN 3: EXACTITUD, TOTALIDAD Y CRONOLOGÍA DE LA INFORMACIÓN

No nos responsabilizamos si la información disponible en este sitio no es precisa, completa o actualizada. El material presentado en este sitio se proporciona solo para información general y no se debe confiar en él ni utilizarlo como la única base para tomar decisiones sin consultar fuentes de información principales, más precisas, más completas o recientes. Al confiar en cualquier material de este sitio lo hace por su cuenta y riesgo. Este sitio puede contener cierta información histórica. La información histórica, inevitablemente, no es actual y se proporciona únicamente como referencia. Nos reservamos el derecho de modificar el contenido de este sitio en cualquier momento, pero no tenemos la obligación de actualizar ninguna información en nuestro sitio. Usted acepta que es su responsabilidad controlar los cambios en nuestro sitio.

SECCIÓN 4: MODIFICACIONES AL SERVICIO Y PRECIOS
 
Los precios de nuestro servicio están sujetos a cambios sin previo aviso. Nos reservamos el derecho de modificar o discontinuar el Servicio (o cualquier parte o contenido de este) sin previo aviso en cualquier momento. No seremos responsables ante usted ni ante ningún tercero por ninguna modificación, cambio de precio, suspensión o interrupción del Servicio.

SECCIÓN 5: ENLACES DE TERCEROS

Algunos contenidos, productos y servicios disponibles a través de nuestro Servicio pueden incluir recursos de terceros. Los enlaces de terceros en este sitio pueden dirigirlo a páginas web de terceros que no están afiliados a nosotros. No somos responsables de examinar o evaluar el contenido o la exactitud, ni garantizamos ni asumiremos ninguna obligación ni responsabilidad por los recursos o páginas web de terceros, ni por ningún otro material, producto o servicio de terceros. No somos responsables de ningún daño o perjuicio relacionado con la compra o el uso de bienes, servicios, recursos, contenido o cualquier otra transacción realizada en conexión con sitios web de terceros. Revise cuidadosamente las políticas y prácticas de terceros, y asegúrese de comprenderlas antes de participar en cualquier transacción. Las quejas, reclamos, inquietudes o preguntas referentes a productos de terceros deben dirigirse a estos.

SECCIÓN 6: INFORMACIÓN PERSONAL

El envío de la información personal que haga a través de nuestras aplicaciones se rige por nuestra Política de privacidad. Para ver nuestra Política de privacidad.

SECCIÓN 7: USOS

Además de las prohibiciones establecidas en los Términos del servicio, se le prohíbe utilizar el sitio o su contenido (a) para cualquier propósito ilegal; (b) para solicitar a otros que realicen o participen en cualquier acto ilegal; (c) para infringir cualquier reglamento, norma, ley u ordenanza
 
local internacional, federal, provincial o estatal; (d) para infringir o violar nuestros derechos de propiedad intelectual o los derechos de propiedad intelectual de otros; (e) acosar, abusar, insultar, dañar, difamar, calumniar, denigrar, intimidar o discriminar por motivos de género, orientación sexual, religión, etnia, raza, edad, nacionalidad o discapacidad; (f) enviar información falsa o engañosa;(g) cargar o transmitir virus o cualquier otro tipo de código dañino que afecte o pueda afectar a la funcionalidad o el funcionamiento del Servicio o de cualquier aplicativo relacionado, de otros sitios web o de Internet; (h) recopilar o rastrear la información personal de otros; (i) enviar correo no deseado, phishing, pharm, pretexto, spider, rastrear o extraer; (j) para cualquier propósito obsceno o inmoral; o (k) para interferir o eludir las funciones de seguridad del Servicio o de cualquier aplicativo relacionado, o de otros sitios web o de Internet. Nos reservamos el derecho de dar por terminado su uso del Servicio o de cualquier aplicativo relacionado por infringir cualquiera de los usos prohibidos.

SECCIÓN 8: DESCARGO DE RESPONSABILIDAD DE GARANTÍAS; LIMITACIÓN DE RESPONSABILIDAD

No garantizamos, representamos ni aseguramos que el uso que haga de nuestro servicio será sin interrupciones, oportuno, seguro o sin errores. No garantizamos que los resultados que se puedan obtener del uso del servicio sean exactos o confiables. Usted acepta que periódicamente, podamos eliminar el servicio por lapsos de tiempo indefinidos o cancelar el servicio en cualquier momento, sin notificarle. Usted acepta expresamente que su uso del servicio o la imposibilidad de utilizarlo corre por su riesgo. El servicio y todos los productos y servicios que se le entregan a través del servicio (salvo que así lo especifiquemos nosotros) se ofrecen "tal como están" y "según disponibilidad" para su uso, sin ninguna representación, garantía o condición de ningún tipo, ya sea expresa o implícita, entre las que se incluyen todas las garantías implícitas o condiciones de comerciabilidad, calidad comercial, idoneidad para un propósito particular, durabilidad, título y no violación. En ningún caso Innovate Whit Proyects, nuestros directores, funcionarios, empleados, afiliados, agentes, contratistas, pasantes, proveedores, proveedores de servicios o
 
licenciantes serán responsables de cualquier lesión, pérdida, reclamo o cualquier daño directo, indirecto, incidental, punitivo, especial o consecuente de cualquier tipo, incluyendo de manera enunciativa más no limitativa; la pérdida de beneficios, pérdida de ingresos, pérdida de ahorros, pérdida de datos, costos de reemplazo o daños similares, ya sea por contrato, perjuicio (incluida la negligencia), responsabilidad estricta o de otro tipo, que surjan del uso que haga de cualquiera de los servicios o de cualquier producto adquirido por medio del servicio, o para cualquier otro reclamo relacionado de alguna manera con su uso del servicio o de cualquier producto, incluidos, entre otros, cualquier error u omisión en cualquier contenido, o cualquier pérdida o daño de cualquier tipo en el que se haya incurrido como resultado del uso del servicio o de cualquier contenido (o producto) publicado, transmitido o puesto a disposición a través del servicio, incluso si se informa de su posibilidad. Debido a que algunos estados o jurisdicciones no permiten la exclusión o la limitación de la responsabilidad por daños consecuentes o incidentales, en dichos estados o jurisdicciones, nuestra responsabilidad se limitará a la extensión máxima de lo permitido por la ley.

SECCIÓN 9: DIVISIBILIDAD

En caso de que se determine que alguna disposición de los presentes Términos del servicio sea ilegal, nula o inaplicable, dicha disposición será, no obstante, ejecutable en la medida en que lo permita la legislación aplicable, y la parte inaplicable se considerará separada de los presentes Términos del servicio, sin que dicha determinación afecte a la validez y aplicabilidad de las demás disposiciones.

SECCIÓN 10: RESCISIÓN

Las obligaciones y responsabilidades de las partes incurridas antes de la fecha de rescisión seguirán vigentes después de la rescisión de este contrato a todos los efectos. Estos Términos del servicio se encuentran vigentes a menos que usted o nosotros los rescindamos. Puede rescindir los presentes Términos del servicio en cualquier momento al notificarnos que ya no desea utilizar nuestros Servicios o cuando cese de utilizar
 
nuestro sitio. Si a nuestro juicio usted incumple, o sospechamos que ha incumplido con cualquier término o disposición de los presentes Términos del servicio, podemos rescindir igualmente este acuerdo en cualquier momento sin previo aviso y usted seguirá siendo responsable de todos los importes adeudados, hasta la fecha de rescisión inclusive; y/o en consecuencia podemos denegarle el acceso a nuestros Servicios (o a parte de ellos).

SECCIÓN 11: ACUERDO COMPLETO

El hecho de que no ejerzamos o hagamos valer algún derecho o disposición de los presentes Términos del Servicio no constituirá una renuncia a dicho derecho o disposición. Estos Términos de servicio y cualquier política o regla de funcionamiento que hayamos publicado en este sitio o con respecto al Servicio constituye el acuerdo y el entendimiento completo entre usted y nosotros, y rigen su uso del Servicio, sustituyendo a cualquier acuerdo, comunicación o propuesta anterior o contemporánea, ya sea oral o escrita, entre usted y nosotros (incluyendo de manera enunciativa más no limitativa, las versiones anteriores de los Términos del servicio).Cualquier ambigüedad en la interpretación de los presentes Términos del servicio no se interpretará en contra de la parte redactora.

SECCIÓN 12: LEY APLICABLE

Los presentes Términos del servicio y cualquier acuerdo por separado por el cual le proporcionemos Servicios se regirán e interpretarán de acuerdo con las leyes de Bucaramanga, Colombia

SECCIÓN 13: CAMBIOS EN LOSTÉRMINOS DEL SERVICIO

Puede revisar la versión más reciente de los Términos del servicio en cualquier momento en esta página. Nos reservamos el derecho, a nuestra entera discreción, de actualizar, cambiar o sustituir cualquier parte de los presentes Términos del servicio mediante la publicación de actualizaciones y cambios en nuestro aplicativo. Es su responsabilidad
 
consultar nuestro aplicativo periódicamente para ver los cambios. El uso que haga de nuestra aplicativo o del Servicio o su acceso a cualquiera de estos de forma continua después de la publicación de cualquier cambio en los presentes Términos del servicio, constituye la aceptación de dichos cambios.
""", width=150, height=40).place(x=170, y=100)
    
    Scrollbar = tk.Scrollbar(Terminos)
    Termininos_Y_Condiciones.mainloop()
Crear_Terminos_Y_Condiciones()