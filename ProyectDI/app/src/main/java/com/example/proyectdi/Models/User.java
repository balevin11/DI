package com.example.proyectdi.Models;

public class User {
    private String id;
    private String name, email, address;
    private int phone;
    
    public User() {}

    public User(String id, String name, String email, String address, int phone) {
        this.id = id;
        this.name=name;
        this.email = email;
        this.phone = phone;
        this.address = address;
    }

    public String getId() { return id; }
    public String getName() { return name; }
    public String getEmail() { return email; }
    public int getPhone() {return phone;}
    public String getAddress() {return address;}

}
