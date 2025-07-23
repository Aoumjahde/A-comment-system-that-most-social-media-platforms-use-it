from instagramBrain import Commentator


while(True):
    try:
        commentMessage = input("Please Entre your message Here : ")
    except:
        exit(0)
    comment = Commentator(commentMessage)

    print("|Add comment|\n|Delete comment|\n|Old comments|\n|Recent comments|\n ")
    try:
        userChioce = int(input("Please Presse |1| * |2| * |3| * |4|: ")) # user check
    except:
        exit(0)

    if userChioce == 1:
        comment.newComment(commentMessage) 
        
    elif userChioce == 2:
        comment.deleteComment()
        pass
    elif userChioce == 3:
        print(comment.oldComment())
        break  # reverse liked list to show old comments to recent
        
    elif userChioce == 4:
        print(comment.recentlyComment())
        break
        
    else:
        exit(0)