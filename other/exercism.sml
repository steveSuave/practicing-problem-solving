(* raise Fail "not yet implemented" *)

fun hello () = "Hello, World!";

(* ================================================================ *)

fun isLeapYear year =
    year mod 4 = 0 andalso
    year mod 100 <> 0 orelse
    year mod 400 = 0;

(* ================================================================ *)

fun name (input: string option) =
    if isSome(input) then
        "One for " ^ valOf(input) ^ ", one for me."
    else
        "One for you, one for me.";

(* ================================================================ *)

datatype planet = Mercury | Venus | Earth | Mars
                  | Jupiter | Saturn | Neptune | Uranus

fun age_on planet seconds =
    let val divisor = case planet of
                          Mercury => 0.2408467
                        | Venus => 0.61519726
                        | Earth => 1.0
                        | Mars => 1.8808158
                        | Jupiter => 11.862615
                        | Saturn => 29.447498
                        | Neptune => 164.79132
                        | Uranus => 84.016846
    in
        real(seconds) / 31557600.0 / divisor
    end;


(* ================================================================ *)

fun isPangram s =
    let fun panHelper _ [] = true
          | panHelper [] _ = false
          | panHelper lc ab = panHelper (List.filter (fn n => n <> hd lc) lc)
                                        (List.filter (fn n => n <> hd lc) ab)
    in
        panHelper (map Char.toLower (explode s)) (explode "abcdefghijklmnopqrstuvwxyz")
    end;
