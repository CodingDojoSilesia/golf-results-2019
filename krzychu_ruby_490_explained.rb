# Convert argument DSL into an array
d = (ARGV[0] + ":,,99").split(":").map { |x| x.split(",") }
k = 0
# Iterate through rows, but keep track where we are in interpreting DSL
# i is a row number
# k tells us how many rows in current DSL command has left
(0..44).map { |i|
  # Decode current DSL command into helper variables
  f, g, h, m = d[0]
  h = h.to_i
  m = m.to_i

  # Decode current DSL command code. Only first letter of the command is needed to distinguish every command.
  o = f[0]

  # Calculate rows left for current DSL command.
  # If k > 1 then just decrease it. Otherwise, the new k value depends on specific command parameters.
  k = (
      k > 1 ? k - 1 :
      o == "m" ? m :
      o == "e" ? g :
      h > 0 ? h : 1).to_i

  def s(i, j)
    # The shape of the egg is encoded as ASCII characters
    "adfhjklmnopqrsstuuuvvwwwwwwwwwwwwwvuutrqomkhd "[i].ord < (j - 29.5).abs + 89
  end

  # Iterate through columns for current row and calculate final character for every column
  print (0..59).map { |j|
    # Are we outside egg?
    s(i, j) ? " " :
    # Are we in a cell which is a neighbour to an outside cell?
    s(i - 1, j) || s(i + 1, j) || s(i, j - 1) || s(i, j + 1) ? "@" :
    # We are inside an egg, so calculate if this is an occupied cell based on current command and position
    o == "v" ||
    o == "z" && (j % (h * 2 + 1) - h).abs == k ||
    o == "c" && j % (h + 1) < h && (k == (h + 1) / 2 || j % (h + 1) == (h - 1) / 2) ||
    o == "h" && j % (m + 1) == 0 ||
    o == "m" && (j % h == 0 || (j / h % 2 < 1 ? k == 1 : k == m)) ? g :
    " "
  }.join + "\n"
  
  # If there are no more rows to be shown in current command, shift the DSL array to the next command
  k > 1 || d.shift
}
