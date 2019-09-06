class MyCircularQueue {
    
    List<Integer> q;
    int head;
    int tail;
    int capacity;
    int count;

    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        q = new ArrayList<Integer>();
        for (int i=0; i<k; i++){
            q.add(null);
        }
        capacity=k;
        count=0;
        head=-1;
        tail=-1;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if (isFull()) return false;
        if (isEmpty()) {
            head++;
            tail++;
        }else if (tail+1==capacity){
            tail=0;
        }else{
            tail++;
        }
        q.set(tail,value);
        count++;
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {
        if (isEmpty()) return false;
        if (count==1){
            q.set(head,null);
            head=-1;
            tail=-1;
            count=0;
        }else if (head+1==capacity){
            q.set(head,null);
            head=0;
            count--;
        }else{
            q.set(head,null);
            head++;
            count--;
        }
        return true;
    }
    
    /** Get the front item from the queue. */
    public int Front() {
        if(isEmpty()) return -1;
        return q.get(head);
    }
    
    /** Get the last item from the queue. */
    public int Rear() {
        if(isEmpty()) return -1;
        return q.get(tail);
    }
    
    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
        return count==0;
    }
    
    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        return count==capacity;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
 