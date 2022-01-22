node *temp=head;
 while(temp!=NULL)
 { //if temp points to head then it has completed a circle,thus a circular linked list.
    if(temp->next==head)
        return true;
    temp=temp->next;
}

return false;
