package Leetcode;

import java.util.Arrays;

public class Check_Distances_Between_Same_Letters_Easy {
    public static void main(String[] args) {
        int[] distance = {1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        String s = "abaccb";
        System.out.println(checkDistances(s, distance));
    }
    public static boolean checkDistances(String s, int[] distance) {
        for (int i = 0; i < distance.length; i++){
            int position = i;
            position += 97;
            char buchstabe = (char) position;
            System.out.println(buchstabe);
            int firstPosition = s.indexOf(buchstabe);
            if (firstPosition < 0)
                continue;
            if (firstPosition + distance[i] + 1 >= s.length())
                return (false);
            System.out.println(firstPosition + " " + firstPosition + distance[i]);
            System.out.println(s.charAt(firstPosition) + " " + s.charAt(firstPosition + distance[i] + 1));
            if (s.charAt(firstPosition) != s.charAt(firstPosition + distance[i] + 1))
                return (false);
            }
        return (true);
        }
    }

