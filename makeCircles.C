void makeTrack(double centerX, double centerY, int sign) {
	TVector2 tracer(-centerX, -centerY);
	TGraph* g = new TGraph(1000);
	TGraph* h = new TGraph(9);

	for (int i=0; i!=1000; ++i) {
		double thisX = centerX + sign*tracer.Rotate(0.00314592*i).X();
		double thisY = centerY + sign*tracer.Rotate(0.00314592*i).Y();
		g->SetPoint(i,thisX,thisY);
	}

	for(int j=0; j!=9; ++j){
		double targetRadius = 0.05+j*0.05;
		int best_i=-1;
		double best_distance=9999.9;
		for(int i=0; i!=1000; ++i){
			double thisRadius = sqrt(pow(g->GetX()[i],2) + pow(g->GetY()[i],2));
			if(fabs(targetRadius-thisRadius) < best_distance){
				best_i = i;
				best_distance = fabs(targetRadius-thisRadius);
			}
			h->SetPoint(j,g->GetX()[best_i],g->GetY()[best_i]);
		}
	}

	//h->Print();
	h->SetMarkerSize(0.6);
	h->Draw("P");
	g->SetLineColor(kBlue);
	g->SetLineStyle(kDashed);
	g->Draw("C");
}

void makeCircles() {

	TCanvas* cv = new TCanvas("cv","cv",600,600);
	cv->Draw();
	TH1F* histo = new TH1F("histo","histo",1,-0.5,0.5);
	histo->SetLineWidth(0);
	histo->Draw();
	histo->GetYaxis()->SetRangeUser(-0.5,0.5);
	for(int i=0; i!=9; ++i){
		TEllipse* e = new TEllipse(0.0,0.0,0.45-i*0.05); 
		e->Draw("SAME");
	}    

	TRandom3 rng;
	for(int nt=0; nt!=80; ++nt) {
		double centerX = 0;	
		double centerY = 0;
		double R = rng.Gaus(0.7,0.04);
		int sign = rng.Uniform(-0.5,0.5) > 0 ? 1 : -1; 
		rng.Circle(centerX, centerY, R);
		makeTrack(centerX, centerY, sign);
	}

	return;
}
