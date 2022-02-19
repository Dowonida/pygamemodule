import pygame
scale=1
pygame.init()
screen = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.SysFont("malgungothic", 32)
img1=pygame.image.load("대출.png")
img2=pygame.image.load("주모.png")
#def command(text1,text2):
 #   print(text1+text2)

def nothing():
    pass
    print("nothing")


class Button:
    def __init__(self,x,y,w=0,h=0,command=nothing,
                 bg=(None,None),font=FONT,image=(None,None),
                 fg=((255,255,255),(0,0,0)),text=''):
                #bg,image,fg는 (비활성화,활성화)        
        self.command=command
        self.BG=bg
        self.font=font
        self.IMG=image
        self.FG=fg
        
        self.text=text
        (self.bg,self.img,self.fg)=(self.BG[0],self.IMG[0],self.FG[0])
        self.txt=self.font.render(text,True,self.fg)

        #별도의 w,h가 없으면 높이,너비는 텍스트에 맞춰서.
        #이미지의 경우는 직접 입력 필수 
        self.rect = self.txt.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.rect.w+=w
        self.rect.h+=h
        
        #아래의 3개의 변수는 pack으로 되돌리기 용도
        self.w=self.rect.w
        self.h=self.rect.h
        self.Text=text
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                (self.bg,self.fg,self.img)=(self.BG[1],self.FG[1],self.IMG[1])
                self.txt=self.font.render(self.text,True,self.fg)
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                self.command()
            (self.bg,self.fg,self.img)=(self.BG[0],self.FG[0],self.IMG[0])
            self.txt=self.font.render(self.text,True,self.fg)

    def draw(self, screen):
        # Blit the text.

        # Blit the rect.
        if self.bg:#배경은 색의 여부로
            pygame.draw.rect(screen, self.bg, self.rect,0)#마지막인수는 두께. 0이면 전부채우고 숫자를 입력하면 해당 두께만큼 테두리 
        if self.img:#이미지는 이미지 존재 여부로 
            screen.blit(self.img,[self.rect.x,self.rect.y])
        if self.txt:#텍스트는 fg가 아니라 text여부로 생성됨 
            screen.blit(self.txt,[self.rect.x,self.rect.y])

    def unpack(self):
        self.text=''
        self.img=None
        self.rect.w=self.rect.h=0
        print("가")

    def pack(self):
        self.text=self.Text
        self.img=self.IMG[0]
        self.rect.w=self.w
        self.rect.h=self.h
        print("나")

###이하는 예제코드니까 참고용 
def main():
    clock = pygame.time.Clock()
    btn1 = Button(100, 100,command=nothing,text="바",bg=(COLOR_ACTIVE,COLOR_INACTIVE))
    btn2 =Button(210,200,100,30,image=(img1,img2))
    btn3= Button(310,300,text="텍스트",bg=((11,11,11),(99,99,0)))
    btn2.command=btn3.unpack
    btn1.command=btn3.pack
    btn3.Text="가나다"
    items = [btn1, btn2,btn3]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                items[1].text="고라니"
            if event.type == pygame.QUIT:
                done = True
            for box in items:
                box.handle_event(event)#모든 객체에 대해 이벤트 실행 


        screen.fill((30, 30, 30))
        for box in items:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pygame.quit()

#원본참고
#https://www.codegrepper.com/code-examples/python/how+to+make+a+text+input+box+python+pygame
