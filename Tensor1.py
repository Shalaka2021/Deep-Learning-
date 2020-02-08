import tensorflow as tf;

with tf.compat.v1.Session() as sobj:
	node1=tf.constant(3.0,tf.float32);
	node2=tf.constant(4.0,tf.float32);

	print(sobj.run([node1,node2]));
	sobj.close()
