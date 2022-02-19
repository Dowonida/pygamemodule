import pygame

chattext=[]
이중모음=list("과괘괴궈궤귀긔")
이중받침=list("갃갅갆갉갊갋갌갍갎갏값")
초성차이=ord("까")-ord("가")
이모=[]
이받=[]
for i in 이중모음:
    이모.append(ord(i)-ord("가"))

for i in 이중받침:
    이받.append(ord(i)-ord("가"))
    
def kcount(a):
    cnt=2
    cs=ord(a)-((ord(a)-520)-(ord(a)-520)%588+520)
    if cs%28 in 이받:
        cnt+=2
    elif cs%28==0:
        cnt+=0
    else:
        cnt+=1
    if cs-cs%28 in 이모:
        cnt+=1
    return cnt

alpkey=[]
for i in range(97,123):
    alpkey.append(i)
for i in range(65,91):
    alpkey.append(i)

pygame.init()
screen = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.SysFont("malgungothic", 32)

#def command(text1,text2):
 #   print(text1+text2)


class InputBox:

    def __init__(self, x, y, w, h,cmd,AlwaysActivated=1):
        self.rect = pygame.Rect(x, y, w, h)
        self.COLOR_INACTIVE=COLOR_INACTIVE
        self.COLOR_ACTIVE=COLOR_ACTIVE
        self.color = COLOR_INACTIVE
        self.text1= self.text2=''
        self.FONT=FONT
        self.txt_surface = self.FONT.render(self.text1+self.text2, True, self.color)
        self.active = False
        self.AA=AlwaysActivated
        self.cmd=cmd

    def entent(self,event):
        global alpkey
        if ord(event.unicode) not in range(ord("가"),ord("힣")+1):
            self.text2 +=event.unicode#한글이 아니면 그냥 추가
            
        else:
            self.text2+=event.unicode  
            k=min(len(self.text2),kcount(event.unicode)+2)
            cnt=''
            for i in range(-k,0):
                if ord(self.text2[i]) not in alpkey:
                    cnt+=self.text2[i]
            self.text2=self.text2[:-k]+cnt                    

            if event.key == pygame.K_SPACE:
                self.text1+=self.text2+' '
                self.text2=''


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
            #if문을 한 줄로 적은 것이다. 해석은 그대로 자연스럽게 
        if event.type == pygame.KEYDOWN:
            if self.active+self.AA:
                if event.key == pygame.K_BACKSPACE:
                    if len(self.text2)>0:
                        self.text2=self.text2[:-1]
                    elif len(self.text1)> 0:
                        self.text1 = self.text1[:-1]
                elif event.key == pygame.K_RETURN or event.key==1073741912:
                    self.cmd(self.text1,self.text2)
                    self.text1=self.text2=''

                    #sendmsg()
                elif event.key == pygame.K_ESCAPE:
                    self.text1=self.text2=''
                else:
                    try:
                        self.entent(event)
                        
                    except:
                        pass
#                entry = font1.render(text1+text2,True,BLACK)
 #               rect1.size = entry.get_size()
  #              cursor1.topleft = rect1.topright

                        # Re-render the text.
                self.txt_surface = self.FONT.render(self.text1+self.text2, True, self.color)

    def update(self):
        # 박스크기 재조정 
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)



###이하는 예제코드니까 참고용 
def main():
    clock = pygame.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32,command)
    input_box2 = InputBox(100, 300, 140, 32,command)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)#모든 객체에 대해 이벤트 실행 

        for box in input_boxes:#전부 업데이트 
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pygame.quit()

#원본참고
#https://www.codegrepper.com/code-examples/python/how+to+make+a+text+input+box+python+pygame
