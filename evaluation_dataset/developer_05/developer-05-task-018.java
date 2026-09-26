public static Profile lookup(String name, File directory) throws IOException {
        List<Profile> profiles = readProfileFromClasspath(name);
        File profileFile = findProfileYaml(directory);
        if (profileFile != null) {
            List<Profile> fileProfiles = fromYaml(new FileInputStream(profileFile));
            for (Profile profile : fileProfiles) {
                if (profile.getName().equals(name)) {
                    profiles.add(profile);
                    break;
                }
            }
        }
        Collections.sort(profiles, Collections.<Profile>reverseOrder());
        return mergeProfiles(profiles);
    }