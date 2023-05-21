// Copyright (c) 2023, Philip Ihesiulo and contributors
// For license information, please see license.txt


//Demographics that have been added to child table
let added_demo = [];

//Demographics that have not been added to child table
let usable_demo = [];

//Documents of demographics that belong to the selected indicator 
let indicator_demo = [];

frappe.ui.form.on('Quarterly Performance', {
	refresh: async (frm) => {
		// Set added_demo if achievement is already provided
		if (is_achievement_provided) {
			added_demo = [...frm.doc.achievements.map(item => item.demo)];	
		}

		// Set users zone
		const logged_in_user = frappe.session.user;
		const atasp_user = await frappe.db.get_doc('ATASP Connect User', logged_in_user);
		const zone = atasp_user.zone;
		frm.set_value('zone', zone);

		//set active indicator's demographics and filter used demographics
		if (frm.doc.indicator) {
			indicator_demo = await get_indicator_demo(frm.doc.indicator);
			set_usable_demo_filter(indicator_demo, frm);
		}
	},

	before_submit: async (frm, cdt, cdn) => {
		// Prevent form from saving if all indicator demographics don't have achievements 
		if (usable_demo.length > 0 || indicator_demo.length > frm.doc.achievements.length) {
			frappe.throw(`You have not provided the achievements for the following indicators: \n ${usable_demo}`);
            return false; 
		}
	},

	indicator: async (frm) => {
		// Remove old achievements if indicator is changed
		if (is_achievement_provided(frm)){
			frm.clear_table('achievements');
			frm.refresh_fields();
		}		

		// Show only indicators related to selected demographic if indicator is selected
		added_demo = [];
		indicator_demo = await get_indicator_demo(frm.doc.indicator);
		set_usable_demo_filter(indicator_demo, frm)

		frm.set_value('outcome', 0);
	}
});

frappe.ui.form.on('Demograhic Achievement', {
    
    achievement (frm, cdt, cdn) {
		// Add to total outcome value
		const indicators = frm.doc.achievements;
		let outcome = 0;
		indicators.forEach(indicator => {
			const achievement = indicator.achievement ? indicator.achievement : 0;
			outcome += achievement;
		});
		frm.set_value('outcome', outcome);
    },

	demo (frm, cdt, cdn) {
		// Filter out selected demographics
		let row = frappe.get_doc(cdt, cdn);
		added_demo.push(row.demo);
		usable_demo = usable_demo.filter(item => !added_demo.includes(item));
		frm.set_query('demo', 'achievements', () => {
			return {
				filters: {
					demo: ['in', usable_demo],
				}
			}
		})
	},
	
	before_achievements_remove (frm, cdt, cdn) {
		// Filter out selected demographics
		let row = frappe.get_doc(cdt, cdn);
		const new_added_demo = added_demo.filter(item => item != row.demo);
		added_demo = new_added_demo;
		usable_demo = usable_demo.filter(item => !added_demo.includes(item));
		const possible_demo = indicator_demo.map(item => item.demographic);
		if (possible_demo.includes(row.demo)) {
			usable_demo.push(row.demo);
		}
	}
})

const set_usable_demo_filter = (indicator_demo, frm) => {
	usable_demo = indicator_demo.map( item => item.demographic);
	usable_demo = usable_demo.filter(item => !added_demo.includes(item));
		frm.set_query('demo', 'achievements', () => {
			return {
				filters: {
					demo: ['in', usable_demo],
				}
			}
		})
}

const get_indicator_demo = async (indicator_name) => { 
	const indicator_obj = await frappe.db.get_doc('Indicator', indicator_name);
	return indicator_obj.demographic;
}

const is_achievement_provided = (frm) => !(frm.doc.achievements.length == 1 && frm.doc.achievements[0].demo == undefined);