char* reverseString(char* s) {
    int head = 0;
    int end = strlen(s)-1;
    while (head<end)
    {
        int temp = s[head];
        s[head] = s[end];
        s[end] = temp;
        head++;
        end--;
    }
    return s;
}