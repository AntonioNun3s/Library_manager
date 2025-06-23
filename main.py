import classes as cl
import os

print("bem vindo ao gerenciador da sua biblioteca")

while True:

    option = None
    option2 = None

    print("o que voce gostaria de fazer?")
    print("1- adicionar um livro ou usuario")
    print("2- remover um livro ou usuario")
    print("3- modificar o aluguel de um usuario")
    print("4- ver todos os livros ou livros alugados ou usuarios")
    print("5- para salvar mudanças")
    print("0- fechar o programa")
    option = input()
    os.system("cls")


    if option == "1":
        while True:
            print("voce deseja adicionar um livro ou usuario?")
            print("1- livro")
            print("2- usuario")
            option2 = input()
            os.system("cls")

            if option2 == "1":

                title = input("insira o titulo do livro: ")
                ID = input("insira o ID do livro: ")
                author = input("o autor do livro: ")
                ISBN = input("o ISBN do livro: ")
                category = input("a categoria do livro: ")

                try:
                    title = str(title)
                    ID = int(ID)
                    author = str(author)
                    ISBN = int(ISBN)
                    category = str(category)
                except ValueError:
                    print("insira valores validos por favor")
                    print()
                    continue

                cl.library.add_book(title, ID, author, ISBN, category)
                print("livro adicionado com sucesso")
                print()

                break

            elif option2 == "2":

                user = input("insira o nome do usuario: ")
                ID = input("insira o ID do usuario: ")

                try:
                    user = str(user)
                    ID = int(ID)

                except ValueError:
                    print("insira valores validos por favor")
                    print()
                    continue

                cl.library.add_user(user, ID)
                print("usuario adicionado com sucesso")
                print()

                break               

            else:
                print("insira uma opção valida por favor")
                print()


    elif option == "2":
    
        while True:
            print("voce deseja remover um livro ou usuario?")
            print("1- livro")
            print("2- usuario")
            option2 = input()
            os.system("cls")  

            if option2 == "1":

                ID = input("insira o ID do livro: ")

                try:
                    ID = int(ID)
                
                except ValueError:
                    print("insira um valor valido por favor")
                    print()
                    continue

                res = cl.library.remove_book(ID)

                if res == 0:
                    print("nao foi possivel achar o livro")
                    print()
                    break

                print("livro removido com sucesso")
                break

            elif option2 == "2":

                ID = input("insira o ID do usuario: ")

                try:
                    ID = int(ID)
                
                except ValueError:
                    print("insira um valor valido por favor")
                    print()
                    continue

                res = cl.library.remove_user(ID)

                if res == 0:
                    print("nao foi possivel achar o usuario")
                    print()
                    break

                print("usuario removido com sucesso")
                break


    elif option == "3":
    
        while True:
            ID = input("insira o ID do usuario: ")

            try:
                ID = int(ID)

            except ValueError:
                print("insira um valor valido por favor")
                print()
                continue
            
            user = cl.library.search_User(ID)

            if user == 0:
                print("nao foi possivel achar o usuario")
                print()
                break

            while True:
                print("voce gostaria de adicionar um livro nos seus alugueis ou remover um livro?")
                print("1- adicionar")
                print("2- remover")
                option2 = input()
                os.system("cls")

                if option2 == "1":

                    ID = input("insira o ID do livro: ")

                    try:
                        ID = int(ID)
                    except ValueError:
                        print("insira um valor valido por favor")
                        print()
                        continue

                    res = user.borrow_book(ID)

                    if res == 2:
                        print("este usuario ja esta no limite de livros")
                        print()
                        break
                    
                    elif res == 0:
                        print("nao foi possivel achar este livro")
                        print()
                        break

                    print("livro adicionado ao usuario com sucesso")
                    break

                elif option2 == "2":

                    ID = input("insira o ID do livro: ")

                    try:
                        ID = int(ID)
                    except ValueError:
                        print("insira um valor valido por favor")
                        print()
                        continue

                    res = user.return_book(ID)

                    if res == 2:
                        print("este usuario nao tem livros para ser removido")
                        print()
                        break
                    
                    elif res == 0:
                        print("nao foi possivel achar este livro")
                        print()
                        break

                    print("livro removido do usuario com sucesso")
                    break
                
                else:
                    print("insira um valor valido por favor")
                    print()
                    continue
            break

    elif option == "4":
        while True:
            print("voce deseja ver os livros, livros alugados, ou usuarios?")
            print("1- livros")
            print("2- livros alugados")
            print("3- usuarios")
            option2 = input()
            os.system("cls")

            if option2 == "1":
                cl.library.print_books()
        
            elif option2 == "2":
                cl.library.print_borr_books()
        
            elif option2 == "3":
                cl.library.print_users()
        
            else:
                print("insira um valor valido por favor")
                print()
                continue
            break

    elif option == "5":
        cl.library.save_data()
        print("dados salvos com sucesso")
        print()

    elif option == "0":
    
        print("fechando programa...")
        break

    else:
        print("insira uma opção valida por favor")
        print()