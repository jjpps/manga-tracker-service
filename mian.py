import excel as file
import draw as felix
import menu as menu


if __name__ == '__main__':    
   felix.manga_tracker_art()
   file.criarExcel()
   data = file.leExcel()
   if(data ==[]):
      menu.abrirMenu()
   else:
      print("atualizar lista de mangas com os resultados mais atuais")
      





