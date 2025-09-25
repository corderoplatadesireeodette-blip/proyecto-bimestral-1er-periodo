import flet as ft


def main(page: ft.Page):
 page.title="Galería"

page.bgcolor=ft.ColorsBLACK45

perdonajes = [
{
}
   "titulo":"Katsuki Bakugo",
   "autor":"Korei Horikoshi",
   "edad":16-17,
   "descripcion":"Orgulloso,explosivo y desidido,estudiante de heroes con gran talento.",
    "imagen":"https://raw.githubusercontent.com/corderoplatadesireeodette-blip/proyecto-bimestral-1er-periodo/refs/heads/main/bakugo%20katsuki.avif"
},
{
  "titulo":"Ben Drowned",
  "autor":"Alexander D. Hall",
  "edad":12,
  "descripcion":."es una entidad sobrenatural que habita en cartucho maldito del videojuego tHE Legend of Zelda",
  "imagen":"https://raw.githubusercontent.com/corderoplatadesireeodette-blip/proyecto-bimestral-1er-periodo/0c7f805393729c9dc664a989581126c7e7d776a4/ben%20drowned.jpg
},
{
  "titulo":"Raito Sakamaki",
  "autor":"Rejet y Otomate",
  "edad":17-18,
  "descripcion":"Raito es uno de los seis hermanos sakamaki,es pelirojo ojos verdes es jugueton pervertido y burlon.",
  "imagen":"https://raw.githubusercontent.com/corderoplatadesireeodette-blip/proyecto-bimestral-1er-periodo/0c7f805393729c9dc664a989581126c7e7d776a4/DIABOLIK%20LOVERS.jpg"
},
{
  "titulo":"Eyeless jack",
  "autor":"Azrael (Mundislander)",
  "edad":20,
  "descripcion":"Ser humanoide con mascaras suele esconderse en la oscuridad y roba organos humanos como riñones a sus victimas".,
  "imagen":"https://raw.githubusercontent.com/corderoplatadesireeodette-blip/proyecto-bimestral-1er-periodo/0c7f805393729c9dc664a989581126c7e7d776a4/eyeless%20jack.jpg"
},
{
  "titulo":"Gojo satoru",
  "autor":"Gege Akutami",
  "edad":28,
  "descripcion":"Es un hechisero de jujutsu es despreucupado,sarcastico y confiado".,
  "imagen":"https://raw.githubusercontent.com/corderoplatadesireeodette-blip/proyecto-bimestral-1er-periodo/0c7f805393729c9dc664a989581126c7e7d776a4/gojo%20satoru.jpg"
},
{
  "titulo":"jeon jungkook,BTS ,",
  "autor":"BigHit Entertainment (HYBE Corporation) ",
  "edad":28,
  "descripcion":"Es cantante,bailarin,conpositor y productor es el miembro mas joven de BTS y uno de los vocalistas principales".,
  "imagen":"https://raw.githubusercontent.com/corderoplatadesireeodette-blip/proyecto-bimestral-1er-periodo/0c7f805393729c9dc664a989581126c7e7d776a4/jeon%20jungkook.jpg"
},
{
   "titulo":"Laughing jack",
   "autor":"Steve Aikins (snuffbomb)",
   "edad":20,
   "descripcion":"Es un payaso siniestro de cabello negro viste de bufon de blanco y negro es cruel y asesino".,
   "imagen":"https://raw.githubusercontent.com/corderoplatadesireeodette-blip/proyecto-bimestral-1er-periodo/0c7f805393729c9dc664a989581126c7e7d776a4/laughing%20jack.jpg"
},
{
    "titulo":"offenderman",
    "autor":"Fans de slenderman",
    "edad":28,
    "descripcion":"Es un ser humanoide muy alto y sin rostro suele ser caballeroso con sus victimas pero es muy perverso".,
    "imagen":"https://raw.githubusercontent.com/corderoplatadesireeodette-blip/proyecto-bimestral-1er-periodo/0c7f805393729c9dc664a989581126c7e7d776a4/offenderman.jpg"
 },
 {
     "titulo":"Sally",
     "autor":"La-Mishi-Mish",
     "edad":8,
     "descripcion":"Es el espiritu de una niña pequeña es dulce,inocente y cariñosa pero tambien se vuelve aterradora y vengativa".,
     "imagen":"https://raw.githubusercontent.com/corderoplatadesireeodette-blip/proyecto-bimestral-1er-periodo/0c7f805393729c9dc664a989581126c7e7d776a4/sally.jpg"
 },
 {
     "titulo":"Toga Himiko",
     "autor":"Korei Horikoshi",
     "edad":17,
     "descripcion":"Es una de las villanas principales obsesivaes,cruel,peligrosa y ala vez es infatil y juguetona".,
     "imagen":"https://raw.githubusercontent.com/corderoplatadesireeodette-blip/proyecto-bimestral-1er-periodo/0c7f805393729c9dc664a989581126c7e7d776a4/toga%20himiko.jpg"
   },
]

indice_actual=[0]

contenedor=ft.container(
content=ft.Column([]),
 width=400,
 height=500,
 bgcolor=ft.colors.purple_400,
 aligment=ft.aligment.center,
 padding=20

)

 boton_siguente=ft.ElevateButton(text="siguiente personaje")

def mostrar_personaje():
    personaje=personajes[indice_actual[0]]
    contenedor.content=ft.column([
        ft.image(src=personaje["imagen"],windth=300,height=300,fit=ft.imsgefit.CONTAIN),
        ft.text(personaje["titulo"],size=20,weight=ft.fonweight.BOLD),
        ft.text(f"Autor:{personaje['autor']}",size=16),
        ft.text(f"Edad:{personaje[edad]}",size=16),
        ft.text(personaje["descripcion"],size=14,italic=True)
    ],aligment=ft.MainaxisAligment.CENTER)

 if indice_actual[0]==len(personajes)-1:

     boton_siguiente.text="volver al inicio"
 else:
     boton_siguiente.text="siguiente personaje"
   page.update()

def siguiente_click(e):
 indice_actual[0]=(indice_actual[0]+1%len(personajes)
   mostrar_personaje()
  boton_siguiente.on_click=siguiente_click
     

  page.add(
   ft.Container(
    content=ft.column([contenedor,
                       boton_siguiente
     
    ],aligment=ft.MainAxisAligment.CENTER,)
    horizontal_aligment=ft.CrossAxisAligment.CENTER,
                       spacing=20
   ),
    aligment=ft.aligmen.center,
    expand=True
   )
) 
  mostrar_personaje()


ft.app(main)





