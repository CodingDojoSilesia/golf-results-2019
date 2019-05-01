// process.argv[2] = "zigzag,c,9:cross,V,5:zigzag,I,5:cross,e,7:hstrip,e,1,1:cross,X,3:vstrip,o:zigzag,A,7:cross,b,7:cross,K,7";
// process.argv[2] = 'empty,3:hstrip,i,7,7:zigzag,L,13:maze,y,7,7:zigzag,j,9';

// This version was passed through https://jscompress.com/ before submission.

// Store shortcut to the abs function as it is used twice
A = Math.abs

// Convert argument DSL into an array
d = (process.argv[2] + ":,,99").split(":").map(l => l.split(","));

// Iterate through rows, but keep track where we are in interpreting DSL
// i is a row number
// k tells us how many rows in current DSL command has left
i = 0
k = 0
for (; i < 45; i++) {
    // Decode current DSL command into helper variables
    [f, g, h, m] = d[0];

    // Decode current DSL command code. Only first letter of the command is needed to distinguish every command.
    o = f[0]

    // Calculate rows left for current DSL command.
    // If k > 1 then just decrease it. Otherwise, the new k value depends on specific command parameters.
    k = (
        k ||
        o == 'm' && m ||
        h ||
        (o == 'e' ? g : 1)
    ) - 1

    // The shape of the egg is determined from egg curve equation (http://www.mathematische-basteleien.de/eggcurves.htm)
    // However, as I wasn't able to find a single equation to cover the curve, I change curve parameters after row 30.
    s = (i, j) => (
        x = i - 21.85,
        y = A(j - 29.5) - 0.6,
        (1 - x * x / 530) < (y * y / (i < 31 ? 850 : 930)) / Math.exp(0.016 * x)
    )

    // Iterate through columns for current row and calculate final character for every column
    console.log([...Array(60)].map((_, j) =>
        // Are we outside egg?
        s(i, j) ? " " :
        // Are we in a cell which is a neighbour to an outside cell?
        i < 1 || j < 1 || j > 58 || s(i - 1, j) || s(i + 1, j) || s(i, j - 1) || s(i, j + 1) ? "@" :
        // We are inside an egg, so calculate if this is an occupied cell based on current command and position
        o == 'v' ||
        (o == 'z' && (A(j % (h * 2 + 1) - h) == k + 1)) ||
        (o == 'c' && ((j % (h * 1 + 1)) < h && (k == (h - 1) / 2 || (j % (h * 1 + 1) == (h - 1) / 2)))) ||
        (o == 'h' && ((j % (m * 1 + 1) == 0))) ||
        (o == 'm' && (!(j % h) || (j / h % 2 < 1 ? !k : k == m - 1))) ? g :
        " "
    ).join(""));

    // If there are no more rows to be shown in current command, shift the DSL array to the next command
    k || d.shift()
}
