void makeExclusions(){
	TCanvas* cv = new TCanvas("cv","cv",800,800);

	// Sempre util fazer um histograma pra setar os eixos (ROOT sux)
	TH1F* dummy = new TH1F("dummy","dummy",1,-1.2,1.2);
	dummy->Draw();
	dummy->SetLineWidth(0);
	dummy->GetYaxis()->SetRangeUser(-1.2,1.2);
	dummy->Draw();

	// Exclusao quadrada centrada na origem
	TGraph* g = new TGraph(5);
	g->SetPoint(0,-1,0);
	g->SetPoint(1,0,1);
	g->SetPoint(2,1,0);
	g->SetPoint(3,0,-1);
	g->SetPoint(4,-1,0);
	g->Draw("LF"); // LF = LINE, FILL.
	// Talvez voce queira usar CURVED, FILL (CF). Mas tome cuidado
	// Neste caso em particular, com quatro pontos, CURVED faz um circulo!
	g->SetFillColorAlpha(kRed,0.5); // Transparencia 0.5

	// Exclusao "tudo acima de uma parabola"
	TGraph* g2 = new TGraph(12);
	g2->SetPoint(1,0,0);
	g2->SetPoint(2,0.1,0.01);
	g2->SetPoint(3,0.2,0.04);
	g2->SetPoint(4,0.3,0.09);
	g2->SetPoint(5,0.4,0.16);
	g2->SetPoint(6,0.5,0.25);
	g2->SetPoint(7,0.6,0.36);
	g2->SetPoint(8,0.7,0.49);
	g2->SetPoint(9,0.8,0.64);
	g2->SetPoint(10,0.9,0.81);
	// Tem que fechar os pontos de uma maneira esperta.
	// Aqui eu coloquei dois pontos dummy que fecham a 
	// parte de cima verticalmente, fora do grafico!
	g2->SetPoint(0,0,100);
	g2->SetPoint(11,0.9,100);
	g2->Draw("LF");
	g2->SetFillColorAlpha(kBlue,0.5); // Transparencia 0.5
	
	cv->Draw();
}
