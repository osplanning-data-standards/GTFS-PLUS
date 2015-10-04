## Agency
Filename: `agency.txt`

 *  Filename MUST be `agency.txt`
 *  File MUST contain a record for each transit agency.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.

File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`agency_id`			| ID that uniquely identifies the transit agency.
`agency_name`		| Contains full name of transit agency.
`agency_url`		| String. Fully qualified URL of agency.
`agency_timezone`	| String. [List of valid values](http//en.wikipedia.org/wiki/List_of_tz_database_time_zones)

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`agency_lang`		| String. Two-letter, ISO 639-1 code for primary language used by agency.  Case-insensitive (both EN and en are accepted)
`agency_phone`		| String. Phone number for agency.
`agency_fare_url`	| String. URL of where fares are defined.

