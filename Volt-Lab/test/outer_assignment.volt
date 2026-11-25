let score = 1;
{
  score = 2;
  let score = 10;
  { score = score + 1; }
  say score;
}
say score;