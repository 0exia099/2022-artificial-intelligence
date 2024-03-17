from sklearn.linear_model import Perceptron

x = [[0,0],[0,1],[1,0],[1,1]]
y = [0,0,0,1]

#퍼셉트론 생성. tol는 종료 조건
clf = Perceptron(tol=1e-3,random_state=0)
#학습 수행
clf.fit(x,y)
#테스트 수행
print(clf.predict(x))