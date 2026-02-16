from typing import List
import heapq

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        need = k - 1
        
        small = []  # max heap (store negatives)
        large = []  # min heap
        total = 0   # sum of elements in small
        
        def add(x):
            nonlocal total
            heapq.heappush(small, -x)
            total += x
            
            if len(small) > need:
                val = -heapq.heappop(small)
                total -= val
                heapq.heappush(large, val)
        
        def remove(x):
            nonlocal total
            if small and x <= -small[0]:
                small.remove(-x)
                heapq.heapify(small)
                total -= x
            else:
                large.remove(x)
                heapq.heapify(large)
            
            if len(small) < need and large:
                val = heapq.heappop(large)
                heapq.heappush(small, -val)
                total += val
        
        ans = float('inf')
        left = 1
        
        for right in range(1, n):
            add(nums[right])
            
            if right - left > dist:
                remove(nums[left])
                left += 1
            
            if len(small) == need:
                ans = min(ans, total)
        
        return nums[0] + ans
# TLE


"""
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef long long ll;

/* ================= TREAP ================= */

typedef struct Node {
    ll val;
    int id;                 // unique id to handle duplicates
    int priority;
    int size;
    ll sum;
    struct Node *l, *r;
} Node;

int get_size(Node* t){ return t ? t->size : 0; }
ll get_sum(Node* t){ return t ? t->sum : 0; }

void update(Node* t){
    if(!t) return;
    t->size = 1 + get_size(t->l) + get_size(t->r);
    t->sum = t->val + get_sum(t->l) + get_sum(t->r);
}

Node* new_node(ll val, int id){
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->id = id;
    n->priority = rand();
    n->size = 1;
    n->sum = val;
    n->l = n->r = NULL;
    return n;
}

/* Order by (val, id) */
int less(ll v1,int id1,ll v2,int id2){
    if(v1!=v2) return v1<v2;
    return id1<id2;
}

/* split: left < key, right >= key */
void split(Node* t,ll val,int id,Node** l,Node** r){
    if(!t){ *l=*r=NULL; return; }
    if(less(t->val,t->id,val,id)){
        split(t->r,val,id,&t->r,r);
        *l=t;
    }else{
        split(t->l,val,id,l,&t->l);
        *r=t;
    }
    update(t);
}

Node* merge(Node* l,Node* r){
    if(!l||!r) return l?l:r;
    if(l->priority > r->priority){
        l->r=merge(l->r,r);
        update(l);
        return l;
    }else{
        r->l=merge(l,r->l);
        update(r);
        return r;
    }
}

Node* insert(Node* t,ll val,int id){
    Node *l,*r;
    split(t,val,id,&l,&r);
    return merge(merge(l,new_node(val,id)),r);
}

Node* erase(Node* t,ll val,int id){
    Node *l,*m,*r;
    split(t,val,id,&l,&r);
    split(r,val,id+1,&m,&r);   // isolate exact node
    if(m){
        Node* tmp=merge(m->l,m->r);
        free(m);
        m=tmp;
    }
    return merge(l,merge(m,r));
}

/* Sum of k smallest */
ll k_smallest_sum(Node* t,int k){
    if(!t||k<=0) return 0;
    if(get_size(t->l)>=k)
        return k_smallest_sum(t->l,k);
    if(get_size(t->l)+1==k)
        return get_sum(t->l)+t->val;
    return get_sum(t->l)+t->val+
           k_smallest_sum(t->r,k-get_size(t->l)-1);
}

/* ================= SOLUTION ================= */

long long minimumCost(int* nums,int n,int k,int dist){

    if(k==1) return nums[0];

    Node* root=NULL;
    ll ans=LLONG_MAX;
    int need=k-2;

    /* Initial window for i=1:
       window = [2 ... 1+dist]
    */
    for(int j=2;j<=dist+1 && j<n;j++)
        root=insert(root,nums[j],j);

    for(int i=1;i<n;i++){

        if(get_size(root)>=need){
            ll sum=k_smallest_sum(root,need);
            ll cost=(ll)nums[0]+nums[i]+sum;
            if(cost<ans) ans=cost;
        }

        /* slide window:
           remove i+1
           add i+dist+1
        */
        if(i+1<n)
            root=erase(root,nums[i+1],i+1);

        if(i+dist+1<n)
            root=insert(root,nums[i+dist+1],i+dist+1);
    }

    return ans;
}


This solution works




Below one is optimal:



#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdbool.h>

#define MAXN 100005
typedef long long ll;

static ll maxHeap[MAXN];   // stores k-1 smallest (as max heap)
static ll minHeap[MAXN];   // stores remaining (as min heap)

static int maxSize, minSize;
static int activeSmall;    // number of active elements in maxHeap
static ll smallSum;

static bool removed[MAXN];     // lazy deletion by index
static bool inSmall[MAXN];     // membership tracker

static void swap_ll(ll *a, ll *b) {
    ll t = *a; *a = *b; *b = t;
}


static void max_up(int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (maxHeap[p] >= maxHeap[i]) break;
        swap_ll(&maxHeap[p], &maxHeap[i]);
        i = p;
    }
}

static void max_down() {
    int i = 0;
    while (1) {
        int best = i;
        int l = 2*i + 1;
        int r = l + 1;
        if (l < maxSize && maxHeap[l] > maxHeap[best]) best = l;
        if (r < maxSize && maxHeap[r] > maxHeap[best]) best = r;
        if (best == i) break;
        swap_ll(&maxHeap[i], &maxHeap[best]);
        i = best;
    }
}

static void max_push(ll x) {
    maxHeap[maxSize] = x;
    max_up(maxSize++);
}

static ll max_pop() {
    ll top = maxHeap[0];
    maxHeap[0] = maxHeap[--maxSize];
    max_down();
    return top;
}


static void min_up(int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (minHeap[p] <= minHeap[i]) break;
        swap_ll(&minHeap[p], &minHeap[i]);
        i = p;
    }
}

static void min_down() {
    int i = 0;
    while (1) {
        int best = i;
        int l = 2*i + 1;
        int r = l + 1;
        if (l < minSize && minHeap[l] < minHeap[best]) best = l;
        if (r < minSize && minHeap[r] < minHeap[best]) best = r;
        if (best == i) break;
        swap_ll(&minHeap[i], &minHeap[best]);
        i = best;
    }
}

static void min_push(ll x) {
    minHeap[minSize] = x;
    min_up(minSize++);
}

static ll min_pop() {
    ll top = minHeap[0];
    minHeap[0] = minHeap[--minSize];
    min_down();
    return top;
}

static void clean_max() {
    while (maxSize > 0) {
        int idx = maxHeap[0] % MAXN;
        if (!removed[idx]) break;
        max_pop();
    }
}

static void clean_min() {
    while (minSize > 0) {
        int idx = minHeap[0] % MAXN;
        if (!removed[idx]) break;
        min_pop();
    }
}

static void balance(int need) {

    clean_max();
    clean_min();

    while (activeSmall > need) {
        clean_max();
        ll x = max_pop();
        int idx = x % MAXN;
        int val = x / MAXN;

        smallSum -= val;
        activeSmall--;
        inSmall[idx] = false;

        min_push(x);
    }

    while (activeSmall < need) {
        clean_min();
        if (minSize == 0) break;

        ll x = min_pop();
        int idx = x % MAXN;
        int val = x / MAXN;

        smallSum += val;
        activeSmall++;
        inSmall[idx] = true;

        max_push(x);
    }

    clean_max();
    clean_min();
}


long long minimumCost(int* nums, int n, int k, int dist) {

    int need = k - 1;

    maxSize = minSize = 0;
    activeSmall = 0;
    smallSum = 0;

    memset(removed, false, sizeof(bool) * n);
    memset(inSmall, false, sizeof(bool) * n);

    int windowEnd = dist + 2;
    if (windowEnd > n) windowEnd = n;

    for (int i = 1; i < windowEnd; i++) {
        ll key = (ll)nums[i] * MAXN + i;
        max_push(key);
        inSmall[i] = true;
        smallSum += nums[i];
        activeSmall++;
    }

    balance(need);

    ll answer = (ll)nums[0] + smallSum;

    for (int i = windowEnd; i < n; i++) {

        int outIdx = i - dist - 1;
        removed[outIdx] = true;

        if (inSmall[outIdx]) {
            smallSum -= nums[outIdx];
            activeSmall--;
        }

        ll key = (ll)nums[i] * MAXN + i;

        clean_max();
        if (maxSize > 0 && key < maxHeap[0]) {
            max_push(key);
            inSmall[i] = true;
            smallSum += nums[i];
            activeSmall++;
        } else {
            min_push(key);
            inSmall[i] = false;
        }

        balance(need);

        ll cost = (ll)nums[0] + smallSum;
        if (cost < answer) answer = cost;
    }

    return answer;
}

"""
