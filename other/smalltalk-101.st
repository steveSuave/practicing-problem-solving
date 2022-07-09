Transcript
        show:'Hello';
        newLine;
        show: 'World'.

'Hello' at:2 put: $a; yourself.

'Hello' at:1 put: $B; at: 5 put: $e; yourself.

1 + (1/2) squared + (1/3) squared + (1/4) squared.

0.0 to: Float pi *2 by: 1/2 do: [:i | Transcript show: i cos; space].

'There are 12 apples.' select: [:c | c isDigit not].

'We humans, we all love apples'
	findString: 'we'
	startingAt: 1
	caseSensitive: false.

'Joe bought {1} apples and {2} oranges' format: {5 . 4}.

(-80 to: 50) asArray.

(1 to: 100) difference: (25 to: 75).

(1 to: 100) select: [:n | n isPrime].

(1 to: 10) collect: [:n | n cubed].

'Zpv!bsf!b!cptt' collect: [:c | (c asciiValue  -1) asCharacter].

|divisors|
divisors := [:n | (1 to: n) select: [:d | n \\ d = 0 ]].
divisors value: 60.

n := 1.
[ n < 1000 ] whileTrue: [ n := n * 2 ].

n := 1.
10 timesRepeat: [ n := n * 2 ].

result := String new.
1 to: 10 do: [:x | result := result, x printString, ' '].
result.
