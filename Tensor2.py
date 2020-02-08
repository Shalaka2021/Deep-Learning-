import tensorflow as tf;

with tf.compat.v1.Session() as sobj:
	node1=tf.constant(3.0,tf.float32);
	node2=tf.constant(4.0,tf.float32);

	ans=node1*node2;

	print(sobj.run(ans));

	sobj.close();