Considerations made:

* The language used for the implementation was Python.
* Units use a State-like model to represent roles (Pikeman, Archer or Knight), as role changes are constrained by domain rules.
* Battles are modeled as an interaction between armies, with Battle acting as lightweight record for history purposes (for Units).
* Army is responsible for orchestrate and enforce domain invariants (owns units and battle rules).
* Civilizations were not explicitly modeled, as they only affect the configuration of an Army and were considered out of scope. If I had to add this concept into this model, an Abstract Factory design pattern would be appropriate to create specific types of Armies (English, Byzantine, or Chinese) with the corresponding initial set of Units.

Assumptions made:
* Armies must be created with at least one unit.
* In case of a draw, each army loses its weakest unit.
* An army cannot attack itself.
