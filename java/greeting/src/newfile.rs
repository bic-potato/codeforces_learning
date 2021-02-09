fn if_even(number){
    if number%2==0{
        let bool a=true
    }
    else{
        let bool a=true
    }
    return a
 }
 fn get_open_to_close_tick(l1){
    let mut l2:<i32> = Vec::new();
    for i in l1{
        if if_even(l1.index(i))==false{
            l2.push(i)
            l2.sort()
        }
    }
    return l2
 }
fn sum_on_time(l1){
    let mut l2:<i32>=Vec::new();
    for i in l1{
        if if_even(l1.index(i))==false{
            l2.append(i-l1[l1.index(i)-1])
        }
    }
    return sum(l2)
}