class CalcentralUser < ActiveRecord::Base
  attr_accessible :firstLogin, :link, :preferredName, :uid

	after_initialize do
		@campus_attributes = CampusPerson.find(self.uid) || {}
	end

	def preferredName
		read_attribute(:preferredName) || @campus_attributes['person_name']
	end

end
