<HTML>
	<BODY>
		<H1> Terrorism Analysis With Insights </H1>
		<H4>
    <I> Data analysts exist at the intersection of information technology, statistics and business. They combination of these fields in order to help businesses 
			and organizations succeed. </I>
    </H4>
		<P> 
			In this, Presentation of a Web App using Python Sciprt & by applying Dash Framework for displaying visualization of data of Global Terrorism data with the help of 
			a DataSet of approximately 2 Lakh records is done. 
		</P>
		<H3><I> Two Types of Visualization methods are being used: </I></H3>
		<UL TYPE = "SQUARE">
			<LI><B> Map </B>
				<UL TYPE = "DISC">	
					<LI> World Map
						<UL TYPE = "CIRCLE">
							<LI><I> Detailed Visualization of Incidents all over the World </I></LI>
						</UL> 
					</LI>
					<LI> India Plot 
						<UL TYPE = "CIRCLE">
							<LI><I> Detailed Visualization of Incidents all over India </I></LI>
						</UL> 
					</LI>
				</UL>
			</LI>
			<LI><B> Area Chart </B>
				<UL TYPE = "DISC">	
					<LI> World Area Chart 
						<UL TYPE = "CIRCLE">
							<LI><I> Visualization of Incident Counts vs Year of Data all over the World </I></LI>
						</UL> 
					</LI>
					<LI> India Area Chart 
						<UL TYPE = "CIRCLE">
							<LI><I> Visualization of Incident Counts vs Year of Data all over India </I></LI>
						</UL> 
					</LI>
				</UL>
			</LI>
		</UL>
		<H3><I> Map User Interface </I></H3>
		<P> 
			The User Inteface Elements in this section plays the role of filtering data for the Map display.
			<BR>User Interface Elements under Map section are: 
		</P>
		<UL TYPE = "DISC">
			<LI><B> DropDowns </B>
				<UL TYPE = "CIRCLE"><I>
					<LI> Month </LI>
					<LI> Date </LI>
					<LI> Region </LI>
					<LI> Country </LI>
					<LI> Province / State </LI>
					<LI> City </LI>
					<LI> Attack-Type </LI>
				</UL></I>
			</LI>
			<LI><B> Year-slider </B>
				<UL TYPE = "CIRCLE">
					<LI><I> Year selection in a range of 1970 to 2018 <I></LI>
				</UL>
			</LI>
			<LI><B> World Graph </B>
				<UL TYPE = "CIRCLE">
					<LI><I> Visualization of the filtered data on Graph </I></LI>
				</UL>
			</LI>	
		</UL>
		<P>
			There are few restrictions in these Dropdowns like the User has to first select Month(s) in order to select Day(s), select Region(s) in order to select Country(ies) 
			and same for the case of Province(s) followed by City(ies).lying in that particular Region. All these filterings are done using Auto-Filtering CallBacks.<BR> 
			Both the India and World Maps have a Legend beside them displaying all the Attack-types and plotted beside the respective Map. <BR>
			<B> India Map: </B> The region is fixed to South Asian region and the Country is set to India, other filters are working same as that of World Map.
		</P>
		<H3><I> Chart User Interface </I></H3>
		<P> 
			The User Inteface Elements in this section plays the role of filtering data categories to be plotted or viewed on Chart.<BR>
			User Interface Elements under Map section are: 
		</P>
		<UL TYPE = "DISC">
			<LI><B> DropDown </B>
				<UL TYPE = "CIRCLE">
					<LI><I> Selection of Type by which the Grouping of data is plotted </I></LI>
				</UL>
			</LI>
			<LI><B> Search Box </B>
				<UL TYPE = "CIRCLE"><I>
					<LI> Works as a filter on plotted data </LI>
				</UL></I>
			</LI>
			<LI><B> Year-slider </B>
				<UL TYPE = "CIRCLE">
					<LI><I> Year selection in a range of 1970 to 2018 <I></LI>
				</UL>
			</LI>
			<LI><B> Area Chart </B>
				<UL TYPE = "CIRCLE">
					<LI><I> Plotted Visualization of the selected data on Chart </I></LI>
				</UL>
			</LI>	
		</UL>
 		<P>
      Both the India and World Charts have a Legend beside them displaying all the required content on basis of category selected in the Dropdown and shown beside the respective Chart. <BR>
      <B> India Chart: </B> The region is fixed to South Asian region and the Country is set to India, other Search box and Year-slider are working same as that of World Chart.
    </P>
	</BODY>
</HTML>
