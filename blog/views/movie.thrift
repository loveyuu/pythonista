# ping service demo
service PingService {
    /*
     * Sexy c style comment
     */
    string ping(1: string name);
    string register2(1: i64 uid, 2: string name, 3: i64 age);
}