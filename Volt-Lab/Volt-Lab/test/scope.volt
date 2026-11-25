let a = "global a";
let b = "global b";
let c = "global c";
{
  let a = "outer a";
  let b = "outer b";
  {
    let a = "inner a";
    say a;
    say b;
    say c;
  }
  say a;
  say b;
  say c;
}
say a;
say b;
say c;