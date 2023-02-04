# 자동차 클래스를 만들어보세요
# 속성(변수) : 차주인, 색상, 차종
# 기능(메서드) : 차정보

#=================================================================

# class 자동차:
#     name = ''
#     color = ''
#     model = ''

#     def 차정보 (self):
#         print(self.name,'의 색상은',self.color,'이고 차종은',self.model,'입니다')
   
#     def 차운전 (self):
#         print(self.name,'가',self.model,'차를 운전합니다')

#     def __init__(self, name, color, model):
#         self.name = name
#         self.color = color
#         self.model = model

# '''
# 사용 예시
# '''

# 아빠차 = 자동차('아빠', 'black', 'gv80')
# 엄마차 = 자동차('엄마', 'red', 'g70')
# 내차 = 자동차('홍길동', 'white', 'k3')

# 아빠차.차정보()     # 차주인, 차색상, 차종  print
# 엄마차.차정보()
# 내차.차정보()       

# 아빠차.차운전()     # 아빠가 차를 운전합니다 print

#=================================================================

class 자동차:
    name = ''
    color = ''
    model = ''
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def 차정보 (self):
        print(self.name,'의 색상은',self.color,'이고 차종은',self.model,'입니다')
        
    def 차운전 (self):
        print(self.name,'가',self.color,'색의',self.model,'차를 운전합니다')

        

'''
사용 예시
'''
# 클래스 사용 예시
아빠차 = 자동차('아빠', 'black', 'gv80')        # 클래스면 옆에 있는 () : __init__생성자
엄마차 = 자동차('엄마', 'red', 'g70')
내차 = 자동차('홍길동', 'white', 'k3')

아빠차.차정보()     # 차주인, 차색상, 차종  print
엄마차.차정보()
내차.차정보()       

아빠차.차운전()     # 아빠가 차를 운전합니다 print
내차.차운전()       # 홍길동 차를 운전합니다 print

# 메서드가 같아도 객체가 다르면 그 객체에 해당하는 메서드와 매개변수로 사용됨