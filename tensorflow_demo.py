import tensorflow as tf

"""
for large and medium no of inputs deep learning is best  if small machine learning is good """

"""
node1=tf.constant(3.0,tf.float32)
node2=tf.constant(4.0,tf.float64)
node3=tf.constant(5.0)

print(node1,node2,node3)

#>>> to run a computational graph
      Session encapsulates the control and state of tensorflow runtime

sess=tf.Session()
print(sess.run([node1,node2,node3]))

"""
"""
n1=tf.constant(2)
n2=tf.constant(3)
n3=tf.constant(4)

n4=tf.multiply(n1,n2)
n5=tf.add(n4,n3)

sess=tf.Session()
output=sess.run(n5)
print(output)
"""

"""
#      Place holders
a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)
s=a+b
sess=tf.Session()
print(sess.run(s,{a:[1,2,3],b:[4,5,6]}))
"""

"""
w=tf.Variable([0.3],tf.float32)
b=tf.Variable([-0.3],tf.float32)

x=tf.placeholder(tf.float32)

linear_model=w*x+b
init=tf.global_variables_initializer()

sess=tf.Session()
sess.run(init)

print(sess.run(linear_model,{x:[1,2,3,4]}))

"""

"""
# it wont run with external(user) inputs

a=tf.constant(4.0)
b=tf.constant(5.0)

c=a*b

sess=tf.Session()

file_writer=tf.summary.FileWriter("C:\\Users\\NIKHIL\\AppData\\Local\\Programs\\Python\\Python36\\graph",sess.graph)

# open cmd and run  ---> tensorboard --logdir="path"

print(sess.run(c))
sess.close()
"""
# placeholder -->  promise to give inputs later
"""
a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)

adder=a+b

sess=tf.Session()

print(sess.run(adder,{a:[1,2],b:[3,4]}))

sess.close()

"""

"""
w=tf.Variable([0.3],tf.float32)
b=tf.Variable([-0.3],tf.float32)

x=tf.placeholder(tf.float32)

linear_model=w*x+b
init=tf.global_variables_initializer()

sess=tf.Session()
sess.run(init)

print(sess.run(linear_model,{x:[1,2,3,4]}))
"""

"""
w=tf.Variable([0.3],tf.float32)
b=tf.Variable([-0.3],tf.float32)

x=tf.placeholder(tf.float32)   

linear_model=w*x+b

y=tf.placeholder(tf.float32)   # actual output of model which we already know

#      loss

square_delta=tf.square(linear_model-y)
loss=tf.reduce_sum(square_delta)

init=tf.global_variables_initializer()   #to initalize

sess=tf.Session()
sess.run(init)
print(sess.run(loss,{x:[4],y:[5]}))
"""

#   optimizer  means computer will reduce loss itself
#   we use gradient descent optimizer
  #   optimzer  will decide value based on change in loss w.r.t change of variable
  # if change of variable increase and loss decreses then it follows that path
  # just like humans   *******


w=tf.Variable([0.3],tf.float32)
b=tf.Variable([-0.3],tf.float32)
aa=[-1,-2,-3,-4]
x=tf.placeholder(tf.float32)   

linear_model=w*x+b

y=tf.placeholder(tf.float32)

square_delta=tf.square(linear_model-y)
loss=tf.reduce_sum(square_delta)

optimizer=tf.train.GradientDescentOptimizer(0.01) # i have to figure why only 0.01
#  0.01 is learning rate   learning rate is from 0.1 - 0.5
train=optimizer.minimize(loss)

init=tf.global_variables_initializer()

sess=tf.Session()
sess.run(init)

for i in range(100):
    sess.run(train,{x:[1,2,3,4],y:aa})

print(sess.run([w,b]))



















