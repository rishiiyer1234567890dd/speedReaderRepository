int i = 0;
String[] file;
String word;
void setup(){
  file = loadStrings("/Users/riyer/test_proj/speedReaderUI/data/text.txt");
  size(600,200);
  textSize(60);
  textAlign(CENTER);
}
void draw(){
    background(255,255,255);
    fill(0);
    if(i < file.length){
      word = file[i];
    }
    else{
      word = "done";
    }
    text(word,width/2,height/2);
    delay(80);
    i++;
}
